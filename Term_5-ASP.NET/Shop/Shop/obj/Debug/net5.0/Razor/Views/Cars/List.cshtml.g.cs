#pragma checksum "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop/Views/Cars/List.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "7980b820275c7157819109232f022b55f8bb00c0"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Cars_List), @"mvc.1.0.view", @"/Views/Cars/List.cshtml")]
namespace AspNetCore
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Rendering;
    using Microsoft.AspNetCore.Mvc.ViewFeatures;
#nullable restore
#line 1 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop/Views/_ViewImports.cshtml"
using Shop.ViewModels;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"7980b820275c7157819109232f022b55f8bb00c0", @"/Views/Cars/List.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"ce6d2fcddf712b9a2d0245bacd50e2caf8d5920d", @"/Views/_ViewImports.cshtml")]
    public class Views_Cars_List : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<dynamic>
    {
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
#nullable restore
#line 7 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop/Views/Cars/List.cshtml"
  
    Layout = "_Layout";

#line default
#line hidden
#nullable disable
            WriteLiteral("\n\n<h1> All auto</h1>\n<h3>");
#nullable restore
#line 13 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop/Views/Cars/List.cshtml"
Write(Model.CurrentCategory);

#line default
#line hidden
#nullable disable
            WriteLiteral("</h3>\n\n");
#nullable restore
#line 15 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop/Views/Cars/List.cshtml"
  
    foreach (var car in Model.AllCars)
    {

#line default
#line hidden
#nullable disable
            WriteLiteral("        <div>\n            <h2> Model: ");
#nullable restore
#line 19 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop/Views/Cars/List.cshtml"
                   Write(car.Name);

#line default
#line hidden
#nullable disable
            WriteLiteral("</h2>\n            <p>price: ");
#nullable restore
#line 20 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop/Views/Cars/List.cshtml"
                 Write(car.Price.ToString("c"));

#line default
#line hidden
#nullable disable
            WriteLiteral("</p>\n        </div>\n");
#nullable restore
#line 22 "/Users/kremenevskiy/Desktop/labs/Term_5-ASP.NET/Shop/Shop/Views/Cars/List.cshtml"
    }

#line default
#line hidden
#nullable disable
        }
        #pragma warning restore 1998
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.IModelExpressionProvider ModelExpressionProvider { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IUrlHelper Url { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IViewComponentHelper Component { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IJsonHelper Json { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<dynamic> Html { get; private set; }
    }
}
#pragma warning restore 1591
