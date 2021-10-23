using Microsoft.AspNetCore.Builder;
using Shop.Middleware;

namespace Shop.Extensions
{
    public static class AppExtensions
    {
        public static IApplicationBuilder UseFileLogging(this IApplicationBuilder app)
            => app.UseMiddleware<LogMiddleware>();
    }
}