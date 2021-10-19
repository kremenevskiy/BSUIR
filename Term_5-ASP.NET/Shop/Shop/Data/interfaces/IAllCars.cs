using System.Collections;
using System.Collections.Generic;
using Shop.Data.Models;

namespace Shop.Data.Models
{
    public interface IAllCars
    {
        IEnumerable<Car> Cars { get; }
        IEnumerable<Car> GetFavouriteCars { get; set; }
        Car GetObjectCar(int carId);

    }
}