using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;

using Shop.Entities;

namespace Shop.Data
{
    // public class ApplicationDbContext : DbContext
    // {
    //     public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
    //     {
    //         
    //     }
    //     public DbSet<Car> Car { get; set; }
    //     public DbSet<Category> Category { get; set; }
    //     public DbSet<ShopCartItem> ShopCartItems { get; set; }
    //     public DbSet<Order> Order { get; set; }
    //     public DbSet<OrderDetail> OrderDetail { get; set; }
    // }
    public class ApplicationDbContext : IdentityDbContext<ApplicationUser>
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
        {
            
        }

        public DbSet<Car> Cars { get; set; }
        public DbSet<CarGroup> CarGroups { get; set; }
        
        public DbSet<Shop.Data.Models.ShopCartItem> ShopCartItems { get; set; }
        public DbSet<Shop.Data.Models.Order> Order { get; set; }
        public DbSet<Shop.Data.Models.OrderDetail> OrderDetail { get; set; }
        
        
        public DbSet<Shop.Data.Models.Car> Car { get; set; }
        public DbSet<Shop.Data.Models.Category> Category { get; set; }
    }
}