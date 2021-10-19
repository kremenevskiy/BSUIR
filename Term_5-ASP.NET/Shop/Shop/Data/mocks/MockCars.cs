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
                        Img = "https://upload.wikimedia.org/wikipedia/commons/9/9c/Tesla_Model_S_Japan.jpg",
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
                        Img = "https://moscowteslaclub.ru/upload/medialibrary/ed2/ed2436e520a9becb9239347c87fcb881.jpeg",
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
                        Img = "https://www.wardsauto.com/sites/wardsauto.com/files/styles/article_featured_retina/public/Taycan_Turbo_S.jpeg",
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
                        Img = "https://img.drivemag.net/media/default/0001/89/Eagle-Squadron-Ford-Mustang-GT-0-2959-default-large.jpeg",
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