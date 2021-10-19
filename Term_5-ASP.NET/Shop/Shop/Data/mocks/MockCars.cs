using System.Collections.Generic;
using System.Linq;
using Shop.Data.Models;

namespace Shop.Data.mocks
{
    public class MockCars : IAllCars
    {
        private readonly ICarsCategory _categoryCars = new MockCategory();
        public IEnumerable<Car> Cars
        {
            get
            {
                return new List<Car>
                {
                    new Car
                    {
                        Name = "Tesla_A",
                        ShortDescription = "Model A",
                        LongDescription = "Electric Model A Tesla",
                        Img = "/img/tesla-s.jpeg",
                        Price = 45000,
                        IsFavourite = true,
                        IsAvailable = true,
                        Category = _categoryCars.AllCategories.First()
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
                        Category = _categoryCars.AllCategories.First()
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
                        Category = _categoryCars.AllCategories.Last()
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
                        Category = _categoryCars.AllCategories.Last()
                    }

                };
            }
            
        }

        public IEnumerable<Car> GetFavouriteCars { get; set; }
        public Car GetObjectCar(int carId)
        {
            throw new System.NotImplementedException();
        }
    }
}