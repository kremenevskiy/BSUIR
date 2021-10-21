using Microsoft.AspNetCore.Mvc;
using Shop.Data.Models;

namespace Shop.Components
{
    public class ShopCartViewComponent : ViewComponent
    {
        private ShopCart _cart;
        public ShopCartViewComponent(ShopCart cart)
        {
            _cart = cart;
        }
        public IViewComponentResult Invoke()
        {
            return View(_cart);
        }
    }
}