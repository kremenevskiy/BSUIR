using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.EntityFrameworkCore;

using Microsoft.EntityFrameworkCore;

namespace Shop.Data.Models
{
    public class ShopCart
    {
        private AppDbContent appDbContent;

        public ShopCart(AppDbContent appDbContent)
        {
            this.appDbContent = appDbContent;
        }
        
        public string ShopCartId { get; set; }
        public List<ShopCartItem> ListShopItems { get; set; }

        public static ShopCart GetCart(IServiceProvider services)
        {
            ISession session = services.GetRequiredService<IHttpContextAccessor>()?.HttpContext.Session;
            var context = services.GetService<AppDbContent>();
            string shopCartId = session.GetString("CartId") ?? Guid.NewGuid().ToString();
            
            session.SetString("CartId", shopCartId);

            return new ShopCart(context) {ShopCartId = shopCartId};
            
        }


        public void AddToCart(Car car)
        {
            this.appDbContent.ShopCartItems.Add(new ShopCartItem
            {
                ShopCartId = this.ShopCartId,
                car = car,
                price = car.Price
            });

            appDbContent.SaveChanges();
        }

        public List<ShopCartItem> GetShopItems()
        {
            return appDbContent.ShopCartItems.Where(c => c.ShopCartId == ShopCartId).Include(s => s.car).ToList();
        }
    }
}