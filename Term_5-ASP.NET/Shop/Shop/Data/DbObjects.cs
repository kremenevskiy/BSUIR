using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Shop.Data.Models;

namespace Shop.Data
{
    public class DbObjects
    {
        public static void Initial(AppDbContent content)
        {
            
            

            if (!content.Category.Any())
            {
                content.Category.AddRange(Categories.Select(c => c.Value));
            }

            if (!content.Car.Any())
            {
                content.AddRange(
                    
                    new Car
                    {
                        Name = "Tesla_A",
                        ShortDescription = "Model A",
                        LongDescription = "Electric Model A Tesla",
                        Img = "/img/tesla-s.jpeg",
                        Price = 45000,
                        IsFavourite = true,
                        IsAvailable = true,
                        Category = Categories["Electric"]
                    },
                    new Car
                    {
                        Name = "Tesla_S",
                        ShortDescription = "Model S",
                        LongDescription = "Electric Model S Tesla",
                        Img = "/img/tesla-a.jpeg",
                        Price = 50000,
                        IsFavourite = true,
                        IsAvailable = true,
                        Category = Categories["Electric"]
                    },
                    new Car
                    {
                        Name = "Porsche_Taycan",
                        ShortDescription = "Porsche Taycan",
                        LongDescription = "New modern model Porsche Taycan",
                        Img = "/img/taycan.jpeg",
                        Price = 100000,
                        IsFavourite = true,
                        IsAvailable = true,
                        Category = Categories["Classic"]
                    },
                    new Car
                    {
                        Name = "Mustang",
                        ShortDescription = "Ford Mustang",
                        LongDescription = "New model Ford Mustang",
                        Img = "/img/mustang.jpeg",
                        Price = 99999,
                        IsFavourite = true,
                        IsAvailable = true,
                        Category = Categories["Classic"]
                    }
                );
            }

            content.SaveChanges();
        }

        private static Dictionary<string, Category> category;
        public static Dictionary<string, Category> Categories
        {
            get
            {
                if (category == null)
                {
                    var categories_list = new Category[]
                    {
                        new Category { CategoryName = "Electric", Description = "Electric Cars"},
                        new Category() { CategoryName = "Classic", Description = "Simple Engine Cars"}
                    };

                    category = new Dictionary<string, Category>();
                    foreach (var el in categories_list)
                    {
                        category.Add(el.CategoryName, el);
                    }
                }

                Console.WriteLine(category);
                return category;
            }
        }
    }
}