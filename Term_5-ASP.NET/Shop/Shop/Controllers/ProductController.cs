using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Shop.Data;
using Shop.Entities;
using Shop.Extensions;
using Shop.Models;

namespace Shop.Controllers
{
    public class ProductController : Controller
    {
        ApplicationDbContext _context;
        int _pageSize;
        
        
        public ProductController(ApplicationDbContext context)
        {
            _context = context;
            _pageSize = 3;
        }
        
        [Route("Catalog")] [Route("Catalog/Page_{pageNo}")]
        public IActionResult Index(int? group, int pageNo=1)
        {
            ViewData["Groups"] = _context.CarGroups;
            ViewData["CurrentGroup"] = group ?? 0;
            var carsFiltered = _context.Cars.Where(d => !group.HasValue || d.CarGroupId == group.Value);
            var model = ListViewModel<Car>.GetModel(carsFiltered, pageNo, _pageSize);
            if (Request.IsAjaxRequest())
                return PartialView("_listpartial", model);
            else
                return View(ListViewModel<Car>.GetModel(carsFiltered, pageNo, _pageSize));
        }
    }
}