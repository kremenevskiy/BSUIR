#pragma checksum "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarDetails.razor" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "94320497ece7a21cdbc896fec0b362117507d74e"
// <auto-generated/>
#pragma warning disable 1591
namespace Shop.Blazor.Client.Components
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Components;
#nullable restore
#line 1 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/_Imports.razor"
using System.Net.Http;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/_Imports.razor"
using System.Net.Http.Json;

#line default
#line hidden
#nullable disable
#nullable restore
#line 3 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/_Imports.razor"
using Microsoft.AspNetCore.Components.Forms;

#line default
#line hidden
#nullable disable
#nullable restore
#line 4 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/_Imports.razor"
using Microsoft.AspNetCore.Components.Routing;

#line default
#line hidden
#nullable disable
#nullable restore
#line 5 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/_Imports.razor"
using Microsoft.AspNetCore.Components.Web;

#line default
#line hidden
#nullable disable
#nullable restore
#line 6 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/_Imports.razor"
using Microsoft.AspNetCore.Components.Web.Virtualization;

#line default
#line hidden
#nullable disable
#nullable restore
#line 7 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/_Imports.razor"
using Microsoft.AspNetCore.Components.WebAssembly.Http;

#line default
#line hidden
#nullable disable
#nullable restore
#line 8 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/_Imports.razor"
using Microsoft.JSInterop;

#line default
#line hidden
#nullable disable
#nullable restore
#line 9 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/_Imports.razor"
using Shop.Blazor.Client;

#line default
#line hidden
#nullable disable
#nullable restore
#line 10 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/_Imports.razor"
using Shop.Blazor.Client.Shared;

#line default
#line hidden
#nullable disable
#nullable restore
#line 11 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/_Imports.razor"
using Shop.Blazor.Client.Models;

#line default
#line hidden
#nullable disable
    public partial class CarDetails : Microsoft.AspNetCore.Components.ComponentBase
    {
        #pragma warning disable 1998
        protected override void BuildRenderTree(Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder __builder)
        {
#nullable restore
#line 1 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarDetails.razor"
 if(Car!=null)
{

#line default
#line hidden
#nullable disable
            __builder.OpenElement(0, "img");
            __builder.AddAttribute(1, "src", 
#nullable restore
#line 3 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarDetails.razor"
               imageSrc

#line default
#line hidden
#nullable disable
            );
            __builder.AddAttribute(2, "class", "img-thumbnail");
            __builder.AddAttribute(3, "width", "150");
            __builder.CloseElement();
            __builder.AddMarkupContent(4, " \n    ");
            __builder.OpenElement(5, "div");
            __builder.OpenElement(6, "p");
            __builder.AddContent(7, 
#nullable restore
#line 5 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarDetails.razor"
            Car.CarName

#line default
#line hidden
#nullable disable
            );
            __builder.AddContent(8, " - ");
            __builder.AddContent(9, 
#nullable restore
#line 5 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarDetails.razor"
                           Car.Description

#line default
#line hidden
#nullable disable
            );
            __builder.CloseElement();
            __builder.AddMarkupContent(10, "\n        ");
            __builder.OpenElement(11, "div");
            __builder.AddAttribute(12, "class", "badge badge-info ");
            __builder.AddMarkupContent(13, "\n            Price: ");
            __builder.AddContent(14, 
#nullable restore
#line 7 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarDetails.razor"
                    Car.Price

#line default
#line hidden
#nullable disable
            );
            __builder.AddMarkupContent(15, " $\n        ");
            __builder.CloseElement();
            __builder.CloseElement();
#nullable restore
#line 10 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarDetails.razor"
}

#line default
#line hidden
#nullable disable
        }
        #pragma warning restore 1998
#nullable restore
#line 12 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarDetails.razor"
       
    [Parameter]
    public DetailsViewModel Car { get; set; }
    [Parameter]
    public EventCallback<DetailsViewModel> CarChanged {get; set;}
    string imageSrc
    {
        get
        {
            return $"images/{Car.Image}";
        } 
    }

#line default
#line hidden
#nullable disable
    }
}
#pragma warning restore 1591