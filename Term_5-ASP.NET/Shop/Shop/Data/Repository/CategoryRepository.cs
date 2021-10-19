using System.Collections.Generic;
using Shop.Data.Models;

namespace Shop.Data.Repository
{
    public class CategoryRepository : ICarsCategory
    {
        private readonly AppDbContent appDbContent;

        public CategoryRepository(AppDbContent appDbContent)
        {
            this.appDbContent = appDbContent;
        }

        public IEnumerable<Category> AllCategories => appDbContent.Category;
    }
}