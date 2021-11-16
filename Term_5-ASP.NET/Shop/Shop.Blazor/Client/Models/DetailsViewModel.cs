using System.Text.Json.Serialization;

namespace Shop.Blazor.Client.Models
{
    public class DetailsViewModel
    {
        [JsonPropertyName("carName")]
        public string CarName { get; set; }
        [JsonPropertyName("description")]
        public string Description { get; set; }
        [JsonPropertyName("price")]
        public int Price { get; set; }
        [JsonPropertyName("image")]
        public string Image { get; set; } 
    }
}