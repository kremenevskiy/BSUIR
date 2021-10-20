using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Mvc;
using Shop.Data.Models;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using Shop.ViewModels;

namespace Shop.Controllers
{
    public class CarsController : Controller
    {
        private readonly IAllCars _allCars;
        private readonly ICarsCategory _allCategories;

        public CarsController(IAllCars iAllCars, ICarsCategory iCarsCategory)
        {
            _allCars = iAllCars;
            _allCategories = iCarsCategory;
        }

        
        [Route("Cars/List")]
        [Route("Cars/List/{carType}")]
        public ViewResult List(string carType)
        {

            string _typeCar = carType;
            IEnumerable<Car> cars;
            string currCategory = "";
            if (string.IsNullOrEmpty(carType))
            {
                cars = _allCars.Cars.OrderBy(i => i.Id);
            }
            else
            {
                if (string.Equals("electro", carType, StringComparison.OrdinalIgnoreCase))
                {
                    cars = _allCars.Cars.Where(i => i.Category.CategoryName.Equals("Electric")).OrderBy(i => i.Id);
                }
                else
                {
                    cars = _allCars.Cars.Where(i => i.Category.CategoryName.Equals("Classic")).OrderBy(i => i.Id);
                }

                currCategory = _typeCar;

                
            }
            
            var carObject = new CarsListViewModel
            {
                AllCars = cars,
                CurrentCategory = currCategory
            };
            
            
            // var cars = _allCars.Cars;
            
            
            ViewBag.Title = "Page with autos";
            return View(carObject);
        }
        
    }
}