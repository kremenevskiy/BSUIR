using System.Collections.Generic;
using Shop.Data.Models;
using System.Linq;
using Microsoft.EntityFrameworkCore;

namespace Shop.Data.Repository
{
    public class CarRepository : IAllCars
    {

        private readonly ApplicationDbContext _applicationDbContext;

        public CarRepository(ApplicationDbContext applicationDbContext)
        {
            this._applicationDbContext = applicationDbContext;
        }

        public IEnumerable<Car> Cars => _applicationDbContext.Car.Include(c => c.Category);
        public IEnumerable<Car> GetFavouriteCars => _applicationDbContext.Car.Where(p => p.IsFavourite).Include(c => c.Category);
        public Car GetObjectCar(int carId) => _applicationDbContext.Car.FirstOrDefault(p => p.Id == carId);

    }
}