using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Mvc;
using Shop.Data.Models;
using System;
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

        public ViewResult List()
        {
            var cars = _allCars.Cars;
            CarsListViewModel obj = new CarsListViewModel();
            obj.AllCars = _allCars.Cars;
            obj.CurrentCategory = "Auto";
            ViewBag.Title = "Page with autos";
            return View(obj);
        }
        
    }
}