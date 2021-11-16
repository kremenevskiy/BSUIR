#pragma checksum "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarsList.razor" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "7c4975ddd30b6e00d6fc6746bf5d66a582f7bb88"
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
    public partial class CarsList : Microsoft.AspNetCore.Components.ComponentBase
    {
        #pragma warning disable 1998
        protected override void BuildRenderTree(Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder __builder)
        {
            __builder.AddMarkupContent(0, "<h3>Cars List</h3>");
#nullable restore
#line 2 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarsList.razor"
 if (Cars == null) {

#line default
#line hidden
#nullable disable
            __builder.AddMarkupContent(1, "<p>Loading ...</p>");
#nullable restore
#line 3 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarsList.razor"
                       }
else
{

#line default
#line hidden
#nullable disable
            __builder.OpenElement(2, "div");
            __builder.AddAttribute(3, "class", "list-group");
#nullable restore
#line 6 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarsList.razor"
                               
        var i = 1;
        foreach (var car in Cars) {

#line default
#line hidden
#nullable disable
            __builder.OpenElement(4, "button");
            __builder.AddAttribute(5, "type", "button");
            __builder.AddAttribute(6, "class", "list-group-item" + " list-group-item-action" + " " + (
#nullable restore
#line 9 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarsList.razor"
                                                                                  SelectedId == car.CarId? "active" : ""

#line default
#line hidden
#nullable disable
            ));
            __builder.AddAttribute(7, "onclick", Microsoft.AspNetCore.Components.EventCallback.Factory.Create<Microsoft.AspNetCore.Components.Web.MouseEventArgs>(this, 
#nullable restore
#line 9 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarsList.razor"
                                                                                                                                       e => Selected(e, car.CarId)

#line default
#line hidden
#nullable disable
            ));
            __builder.AddContent(8, 
#nullable restore
#line 10 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarsList.razor"
                  i++

#line default
#line hidden
#nullable disable
            );
            __builder.AddContent(9, " - ");
            __builder.AddContent(10, 
#nullable restore
#line 10 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarsList.razor"
                          car.CarName

#line default
#line hidden
#nullable disable
            );
            __builder.CloseElement();
#nullable restore
#line 12 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarsList.razor"
        }
                             

#line default
#line hidden
#nullable disable
            __builder.CloseElement();
#nullable restore
#line 15 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarsList.razor"
}

#line default
#line hidden
#nullable disable
        }
        #pragma warning restore 1998
#nullable restore
#line 16 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Components/CarsList.razor"
       
    [Parameter]
    public IEnumerable<ListViewModel> Cars { get; set; }
    [Parameter]
    public EventCallback<IEnumerable<ListViewModel>> CarsChanged { get; set; } 
    
    private int SelectedId = 0;
    [Parameter]
    public EventCallback<int> SelectedObjectChanged { get; set; }
    private void Selected(MouseEventArgs e, int id)
    {
        SelectedId = id;
        SelectedObjectChanged.InvokeAsync(id);
    }


#line default
#line hidden
#nullable disable
    }
}
#pragma warning restore 1591
