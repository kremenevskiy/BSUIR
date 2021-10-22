using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Identity;
using Shop.Entities;

namespace Shop.Data
{
    public class DbInitializer
    {
        public static async Task Seed(ApplicationDbContext context,
            UserManager<ApplicationUser> userManager,
            RoleManager<IdentityRole> roleManager)
        {
            context.Database.EnsureCreated();
            if (!context.Roles.Any())
            {
                var roleAdmin = new IdentityRole
                {
                    Name = "admin",
                    NormalizedName = "admin"
                };
                await roleManager.CreateAsync(roleAdmin);
                await context.SaveChangesAsync();
            }

            if (!context.Users.Any())
            {
                var user = new ApplicationUser
                {
                    Email = "user@mail.ru",
                    UserName = "user@mail.ru"
                };
                await userManager.CreateAsync(user, "123456");
                var admin = new ApplicationUser
                {
                    Email = "admin@mail.ru",
                    UserName = "admin@mail.ru"
                };
                await userManager.CreateAsync(admin, "123456");
                admin = await userManager.FindByEmailAsync("admin@mail.ru");
                await userManager.AddToRoleAsync(admin, "admin");
                await context.SaveChangesAsync();
            }

            if (!context.CarGroups.Any())
            {
                context.CarGroups.AddRange(new List<CarGroup>
                {
                    new CarGroup {GroupName = "Classic"},
                    new CarGroup {GroupName = "Electric"}
                });
                await context.SaveChangesAsync();
            }
            
            if (!context.Cars.Any())
            {
                context.Cars.AddRange(new List<Car>
                {
                    new Car
                    {
                        CarName = "Tesla Model S", Price = 99999, CarGroupId = 2,
                        Description = "Young and Fast", Image = "tesla-s.jpeg",
                    },
                    new Car
                    {
                        CarName = "Tesla Model 3", Price = 11111, CarGroupId = 2,
                        Description = "60 km in 2 secs", Image = "tesla-3.jpeg",
                    },
                    new Car
                    {
                        CarName = "Tesla Model X", Price = 666666, CarGroupId = 2,
                        Description = "Devil's Strongest Car", Image = "tesla-X.jpeg",
                    },
                    new Car
                    {
                        CarName = "Tesla Model Cybertruck", Price = 1000000, CarGroupId = 2,
                        Description = "Meet new Halk", Image = "tesla-cybertrack.jpeg",
                    },
                    new Car
                    {
                        CarName = "Porsche 911 Turbo", Price = 100999, CarGroupId = 1,
                        Description = "Porsche 911... No words", Image = "porsche-911.jpeg",
                    },
                    new Car
                    {
                        CarName = "Ford Mustang", Price = 101010, CarGroupId = 1,
                        Description = "Meet new Ford", Image = "mustang.jpeg",
                    },
                    new Car
                    {
                        CarName = "Ferrari 812-gts", Price = 200000, CarGroupId = 1,
                        Description = "Fresh from Lemon", Image = "ferrari-812-gts.jpeg",
                    },
                    new Car
                    {
                        CarName = "lamborghini Aventador", Price = 450000, CarGroupId = 1,
                        Description = "For real boys", Image = "lamborghini_aventador.jpeg",
                    },
                    new Car
                    {
                        CarName = "Aston Martin", Price = 900000, CarGroupId = 1,
                        Description = "Take sex every trip", Image = "aston-martin.jpeg",
                    }
                });
                await context.SaveChangesAsync();
            }
        }
    }
}