// <auto-generated/>
#pragma warning disable 1591
#pragma warning disable 0414
#pragma warning disable 0649
#pragma warning disable 0169

namespace Shop.Blazor.Client.Pages
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
#nullable restore
#line 1 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Pages/Counter.razor"
using System.ComponentModel.DataAnnotations;

#line default
#line hidden
#nullable disable
    [Microsoft.AspNetCore.Components.RouteAttribute("/counter")]
    public partial class Counter : Microsoft.AspNetCore.Components.ComponentBase
    {
        #pragma warning disable 1998
        protected override void BuildRenderTree(Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder __builder)
        {
        }
        #pragma warning restore 1998
#nullable restore
#line 19 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop.Blazor/Client/Pages/Counter.razor"
       
    private int currentCount = 0;
    private FormModel formModel;
    protected override void OnInitialized()
    {
        formModel=new();
    }
    private void IncrementCount()
    {
        currentCount ++;
    }
    class FormModel
    {
        [DataType("int")] [Range(0,int.MaxValue)]
        public int NewValue { get; set; }
    }
    private void SetCounter()
    {
        currentCount = formModel.NewValue;
    }

#line default
#line hidden
#nullable disable
    }
}
#pragma warning restore 1591