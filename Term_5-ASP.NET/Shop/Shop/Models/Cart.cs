using System.Collections.Generic;
using System.Linq;
using Shop.Entities;

namespace Shop.Models
{
    public class Cart
    {
        public Dictionary<int, CartItem> Items { get; set; } = new Dictionary<int, CartItem>();
        
        public int Count
        {
            get
            {
                return Items.Sum(item => item.Value.Quantity);
            }
        }
        
        public int TotalPrice
        {
            get
            {
                return Items.Sum(item => item.Value.Quantity * item.Value.Car.Price); 
            }
        }
        
        public virtual void AddToCart(Car car)
        {
            if (Items.ContainsKey(car.CarId))
                Items[car.CarId].Quantity++;
            else
                Items.Add(car.CarId, new CartItem
                {
                    Car = car,
                    Quantity = 1
                });
        }
        
        public virtual void RemoveFromCart(int id)
        {
            Items.Remove(id);
        }

        protected virtual void ClearAll()
        {
            Items.Clear();
        }
    }
    
    
}