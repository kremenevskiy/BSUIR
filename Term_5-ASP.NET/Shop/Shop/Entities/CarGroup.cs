using System.Collections.Generic;

namespace Shop.Entities
{
    public class CarGroup
    {
        public int CarGroupId { set; get; }
        public string GroupName { set; get; }
        // public string Description { set; get; }
        public List<Car> Cars { set; get; }
    }
}