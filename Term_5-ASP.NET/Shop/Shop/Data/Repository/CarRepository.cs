using System.Collections.Generic;
using Shop.Data.Models;
using System.Linq;
using Microsoft.EntityFrameworkCore;

namespace Shop.Data.Repository
{
    public class CarRepository : IAllCars
    {

        private readonly AppDbContent appDbContent;

        public CarRepository(AppDbContent appDbContent)
        {
            this.appDbContent = appDbContent;
        }

        public IEnumerable<Car> Cars => appDbContent.Car.Include(c => c.Category);
        public IEnumerable<Car> GetFavouriteCars => appDbContent.Car.Where(p => p.IsFavourite).Include(c => c.Category);
        public Car GetObjectCar(int carId) => appDbContent.Car.FirstOrDefault(p => p.Id == carId);

    }
}