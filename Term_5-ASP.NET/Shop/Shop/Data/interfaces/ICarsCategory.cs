using System.Collections;
using System.Collections.Generic;
using Shop.Data.Models;

namespace Shop.Data.Models
{
    public interface ICarsCategory
    {
        IEnumerable<Category> AllCategories { get; }
        
    }
}