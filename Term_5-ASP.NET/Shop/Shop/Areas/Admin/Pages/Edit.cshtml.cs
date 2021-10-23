using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using Shop.Data;
using Shop.Entities;

namespace Shop.Areas.Admin.Pages
{
    public class EditModel : PageModel
    {
        private readonly Shop.Data.ApplicationDbContext _context;
        private IWebHostEnvironment _environment;

        public EditModel(Shop.Data.ApplicationDbContext context, IWebHostEnvironment env)
        {
            _context = context;
            _environment = env;
        }

        [BindProperty]
        public Car Car { get; set; }
        [BindProperty]
        public IFormFile Image { get; set; }

        public async Task<IActionResult> OnGetAsync(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            Car = await _context.Cars
                .Include(c => c.CarGroup).FirstOrDefaultAsync(m => m.CarId == id);

            if (Car == null)
            {
                return NotFound();
            }
           ViewData["CarGroupId"] = new SelectList(_context.CarGroups, "CarGroupId", "CarGroupId");
            return Page();
        }

        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see https://aka.ms/RazorPagesCRUD.
        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                return Page();
            }
            if (Image != null)
            {
                var fileName = $"{Car.CarId}" + Path.GetExtension(Image.FileName);
                Car.Image = fileName;
                var path = Path.Combine(_environment.WebRootPath, "Images", fileName);
                using (var fStream = new FileStream(path, FileMode.Create))
                {
                    await Image.CopyToAsync(fStream);
                }
            }

            _context.Attach(Car).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!CarExists(Car.CarId))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return RedirectToPage("./Index");
        }

        private bool CarExists(int id)
        {
            return _context.Cars.Any(e => e.CarId == id);
        }
    }
}
