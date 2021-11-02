using System;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Shop.Data;
using Shop.Data.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using Shop.Data.Repository;
using Shop.Entities;
using Shop.Extensions;
using Shop.Models;
using Shop.Services;


namespace Shop
{
    public class Startup
    {

        private IConfigurationRoot _confstring;
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }         
        
        

        
        
        
       
        
        public IConfiguration Configuration { get; }
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddDbContext<ApplicationDbContext>(options =>
                options.UseSqlServer(Configuration.GetConnectionString("DefaultConnection")));
            
            
            services.AddIdentity<ApplicationUser, IdentityRole>(options =>
            {
                options.SignIn.RequireConfirmedAccount = false;
                options.Password.RequireLowercase = false;
                options.Password.RequireNonAlphanumeric = false;
                options.Password.RequireUppercase = false;
                options.Password.RequireDigit = false;
            }).AddEntityFrameworkStores<ApplicationDbContext>().AddDefaultTokenProviders();
            
            services.AddAuthorization();
            services.AddControllersWithViews();
            
            services.AddRazorPages();
            services.ConfigureApplicationCookie(options =>
            {
                options.LoginPath = $"/Identity/Account/Login";
                options.LogoutPath = $"/Identity/Account/Logout";
            });
            
            services.AddDistributedMemoryCache();
            services.AddSession(opt =>
            {
                opt.Cookie.HttpOnly = true;
                opt.Cookie.IsEssential = true;
            });
            
            services.AddSingleton<IHttpContextAccessor, HttpContextAccessor>();
            
            services.AddTransient<IAllCars, CarRepository>();
            services.AddTransient<ICarsCategory, CategoryRepository>();
            services.AddTransient<IAllOrders, OrdersRepository>();

           
            services.AddScoped(sp => ShopCart.GetCart(sp));
            services.AddScoped<Cart>(sp=>CartService.GetCart(sp));
            
            // services.AddMvc();
            // services.AddMvc(options => options.EnableEndpointRouting = false); // хзхзхз без этого не запускалось
            services.AddMemoryCache();


        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app,
                                IWebHostEnvironment env,
                                ApplicationDbContext context,
                                UserManager<ApplicationUser> userManager,
                                RoleManager<IdentityRole> roleManager,
                                ILoggerFactory logger)
        {
            logger.AddFile("Logs/log-{Date}.txt");

            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
                // app.UseMigrationsEndPoint();
                
            }
            app.UseHttpsRedirection();
            app.UseStaticFiles();
            
            // app.UseMvc(routes =>
            // {
            //     routes.MapRoute(name: "default", template: "{controller=Home}/{action=Index}/{id?}");
            //     routes.MapRoute(name: "categoryFilter", template: "Car/{action}/{carType?}",
            //         defaults: new {Controller = "Car", action = "List"});
            // });
            
            app.UseStatusCodePages();

            app.UseRouting();
            app.UseAuthentication();
            app.UseSession();
            app.UseAuthorization();
            // app.UseMvcWithDefaultRoute(); // default index.html if no url with controller and view
            
            // using (var scope = app.ApplicationServices.CreateScope())
            // {
            //     var content = scope.ServiceProvider.GetRequiredService<ApplicationDbContext>();
            //     DbObjects.Initial(content);
            // }
            app.UseFileLogging();

            DbInitializer.Seed(context, userManager, roleManager).Wait();
            app.UseEndpoints(endpoints =>
            {
                // endpoints.MapGet("/", async context => { await context.Response.WriteAsync("Hello World!"); });
                endpoints.MapControllerRoute(
                    name: "default",
                    pattern: "{controller=Home}/{action=Index}/{id?}");
                endpoints.MapRazorPages();
            });
        }
        
    }
}