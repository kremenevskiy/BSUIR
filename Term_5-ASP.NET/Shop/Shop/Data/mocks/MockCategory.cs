using System.Collections.Generic;
using Shop.Data.Models;

namespace Shop.Data.mocks
{
    public class MockCategory : ICarsCategory

    {
        public IEnumerable<Category> AllCategories
        {
            get
            {
                return new List<Category>
                {
                    new Category
                    {
                        CategoryName = "Electric",
                        Description = "New Electric Cars"
                    },
                    new Category()
                    {
                        CategoryName = "Classic",
                        Description = "Simple Engine Cars"
                    }
                };
            }
        }
    }
}