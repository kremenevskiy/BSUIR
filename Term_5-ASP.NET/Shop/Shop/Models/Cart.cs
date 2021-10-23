using System.Collections.Generic;
using System.Linq;
using Shop.Entities;

namespace Shop.Models
{
    public class Cart
    {
        public Dictionary<int, CartItem> Items { get; set; }
        public Cart()
        {
            Items = new Dictionary<int, CartItem>();
        }
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
        
        
        virtual public void AddToCart(Car car)
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
        virtual public void RemoveFromCart(int id)
        {
            Items.Remove(id);
        }
        virtual public void ClearAll()
        {
            Items.Clear();
        }
    }
    
    
}