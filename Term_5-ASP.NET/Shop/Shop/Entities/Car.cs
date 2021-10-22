namespace Shop.Entities
{
    public class Car
    {
        public int CarId { set; get; }
        public string CarName { set; get; }
        // public string ShortDescription { set; get; }
        // public string LongDescription { set; get; }
        public string Description { set; get; }
        public string Image { set; get; }
        public int Price { set; get; }
        // public bool IsFavourite { set; get; }
        // public bool IsAvailable { set; get; }
        public int CarGroupId { set; get; }
        public CarGroup CarGroup { set; get; }
    
    }
}