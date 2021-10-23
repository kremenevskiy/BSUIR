using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Shop.Data;
using Shop.Extensions;
using Shop.Models;

namespace Shop.Controllers
{
    public class CartController : Controller
    {
        private ApplicationDbContext _context;
        private Cart _cart;
        // private string cartKey = "cart";
        
        public CartController(ApplicationDbContext context, Cart cart)
        {
            _context = context;
            _cart = cart;
        }
        
        public IActionResult Index()
        {
            // _cart = HttpContext.Session.Get<Cart>(cartKey);
            return View(_cart.Items.Values);
        }
        
        [Authorize]
        public IActionResult Add(int id, string returnUrl)
        {
            // _cart = HttpContext.Session.Get<Cart>(cartKey);
            var item = _context.Cars.Find(id);
            if (item != null)
            {
                _cart.AddToCart(item);
                // HttpContext.Session.Set<Cart>(cartKey, _cart);
            }
            return Redirect(returnUrl);
        }
        
        public IActionResult Delete(int id)
        {
            _cart.RemoveFromCart(id);
            return RedirectToAction("Index");
        }
    }
}