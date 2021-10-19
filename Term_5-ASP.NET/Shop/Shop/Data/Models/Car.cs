namespace Shop.Data.Models
{
    public class Car
    {
        public int Id { set; get; }
        public string Name { set; get; }
        public string ShortDescription { set; get; }
        public string LongDescription { set; get; }
        public string Img { set; get; }
        public uint Price { set; get; }
        public bool IsFavourite { set; get; }
        public bool IsAvailable { set; get; }
        public bool CategoryId { set; get; }
        public virtual Category Category { set; get; }
        
        
        
    }
}