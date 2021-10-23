using Microsoft.AspNetCore.Mvc;
using Shop.Extensions;
using Shop.Models;

namespace Shop.Components
{
    public class CartViewComponent : ViewComponent
    {
        private Cart _cart;
        public CartViewComponent(Cart cart)
        {
            _cart = cart;
        }
        public IViewComponentResult Invoke()
        {
            // var cart = HttpContext.Session.Get<Cart>("cart");
            return View(_cart);
        }
    }
}