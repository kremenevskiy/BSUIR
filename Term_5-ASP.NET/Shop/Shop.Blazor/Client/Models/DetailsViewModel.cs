using System.Text.Json.Serialization;

namespace Shop.Blazor.Client.Models
{
    public class DetailsViewModel
    {
        [JsonPropertyName("carName")]
        public string CarName { get; set; }
        public string Description { get; set; }
        public int Price { get; set; } 
        public string Image { get; set; } 
    }
}