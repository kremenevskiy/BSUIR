using Shop.Entities;

namespace Shop.Models
{
    public class CartItem
    {
        public Car Car{ get; set; }
        public int Quantity { get; set; }
    }
}