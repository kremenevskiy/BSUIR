using System;
using Shop.Data.Models;

namespace Shop.Data.Repository
{
    public class OrdersRepository : IAllOrders
    {
        private readonly ApplicationDbContext _applicationDbContext;
        private readonly ShopCart shopCart;

        public OrdersRepository(ApplicationDbContext applicationDbContext, ShopCart shopCart)
        {
            this._applicationDbContext = applicationDbContext;
            this.shopCart = shopCart;
        }
        
        public void CreateOrder(Order order)
        {
            order.OrderTime = DateTime.Now;
            _applicationDbContext.Order.Add(order);

            var items = shopCart.ListShopItems; // no items?
            
            foreach (var el in items)
            {
                var orderDetail = new OrderDetail()
                {
                    CarId = el.car.Id,
                    OrderId = order.Id,
                    Price = el.car.Price
                };
                _applicationDbContext.OrderDetail.Add(orderDetail);
            }

            _applicationDbContext.SaveChanges();

        }
    }
}