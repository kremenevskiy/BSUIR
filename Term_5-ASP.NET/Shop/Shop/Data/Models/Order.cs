using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using Microsoft.AspNetCore.Mvc.ModelBinding;

namespace Shop.Data.Models
{
    public class Order
    {
        [BindNever]
        public int Id { get; set; }
        
        [Display(Name = "Enter name")]
        [StringLength(10)]
        [Required(ErrorMessage = "Min lenght: 3")]
        public string Name { get; set; }
        
        [Display(Name = "Surname")]
        [StringLength(10)]
        [Required(ErrorMessage = "Min lenght: 3")]
        public string Surname { get; set; }
        
        [Display(Name = "Address")]
        [StringLength(15)]
        [Required(ErrorMessage = "Min lenght: 5")]
        public string Address { get; set; }
        
        [Display(Name = "Phone Number")]
        [DataType(DataType.PhoneNumber)]
        [StringLength(22)]
        [Required(ErrorMessage = "Min lenght: 7")]
        public string Phone { get; set; }
        
        [Display(Name = "Email")]
        [DataType(DataType.EmailAddress)]
        [StringLength(30)]
        [Required(ErrorMessage = "Min lenght: 4")]
        public string Email { get; set; }
        
        [BindNever]
        [ScaffoldColumn(false)]
        public DateTime OrderTime { get; set; }
        
        public List<OrderDetail> OrderDetails { get; set; }
        
    }
}