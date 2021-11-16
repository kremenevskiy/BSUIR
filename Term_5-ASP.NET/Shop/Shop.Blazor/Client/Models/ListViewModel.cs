using System.Text.Json.Serialization;

namespace Shop.Blazor.Client.Models
{
    public class ListViewModel
    {
        [JsonPropertyName("carId")]
        public int CarId { get; set; } 

        public string CarName { get; set; } 
    }
}