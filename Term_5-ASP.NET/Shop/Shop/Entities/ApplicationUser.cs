using Microsoft.AspNetCore.Identity;

namespace Shop.Entities
{
    public class ApplicationUser:IdentityUser
    {
        public byte[] AvatarImage { get; set; }
    }
}