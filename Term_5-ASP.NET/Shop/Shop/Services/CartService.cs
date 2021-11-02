using System;
using System.Text.Json.Serialization;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using Shop.Entities;
using Shop.Models;
using Shop.Extensions;

namespace Shop.Services
{
    public class CartService : Cart
    {
        private string sessionKey = "cart";
        
        [JsonIgnore]
        ISession Session { get; set; }
        
        public static Cart GetCart(IServiceProvider sp)
        {
            var session = sp.GetRequiredService<IHttpContextAccessor>().HttpContext.Session;
            var cart = session.Get<CartService>("cart") ?? new CartService();
            cart.Session = session;
            return cart;
        }
        
        public override void AddToCart(Car car)
        {
            base.AddToCart(car);
            Session?.Set(sessionKey, this); 
        }
        public override void RemoveFromCart(int id)
        {
            base.RemoveFromCart(id);
            Session?.Set(sessionKey, this); 
        }

        protected override void ClearAll()
        {
            base.ClearAll();
            Session?.Set(sessionKey, this); 
        }
    }
}