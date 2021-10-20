using Microsoft.EntityFrameworkCore.Migrations;

namespace Shop.Migrations
{
    public partial class Order_2 : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_OrderDetail_Order_orderId",
                table: "OrderDetail");

            migrationBuilder.RenameColumn(
                name: "price",
                table: "OrderDetail",
                newName: "Price");

            migrationBuilder.RenameColumn(
                name: "orderId",
                table: "OrderDetail",
                newName: "OrderId");

            migrationBuilder.RenameColumn(
                name: "id",
                table: "OrderDetail",
                newName: "Id");

            migrationBuilder.RenameIndex(
                name: "IX_OrderDetail_orderId",
                table: "OrderDetail",
                newName: "IX_OrderDetail_OrderId");

            migrationBuilder.RenameColumn(
                name: "surname",
                table: "Order",
                newName: "Surname");

            migrationBuilder.RenameColumn(
                name: "phone",
                table: "Order",
                newName: "Phone");

            migrationBuilder.RenameColumn(
                name: "orderTime",
                table: "Order",
                newName: "OrderTime");

            migrationBuilder.RenameColumn(
                name: "name",
                table: "Order",
                newName: "Name");

            migrationBuilder.RenameColumn(
                name: "email",
                table: "Order",
                newName: "Email");

            migrationBuilder.RenameColumn(
                name: "address",
                table: "Order",
                newName: "Address");

            migrationBuilder.RenameColumn(
                name: "id",
                table: "Order",
                newName: "Id");

            migrationBuilder.AlterColumn<string>(
                name: "Surname",
                table: "Order",
                type: "nvarchar(10)",
                maxLength: 10,
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "nvarchar(max)",
                oldNullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "Phone",
                table: "Order",
                type: "nvarchar(22)",
                maxLength: 22,
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "nvarchar(max)",
                oldNullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "Name",
                table: "Order",
                type: "nvarchar(10)",
                maxLength: 10,
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "nvarchar(max)",
                oldNullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "Email",
                table: "Order",
                type: "nvarchar(30)",
                maxLength: 30,
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "nvarchar(max)",
                oldNullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "Address",
                table: "Order",
                type: "nvarchar(15)",
                maxLength: 15,
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "nvarchar(max)",
                oldNullable: true);

            migrationBuilder.AddForeignKey(
                name: "FK_OrderDetail_Order_OrderId",
                table: "OrderDetail",
                column: "OrderId",
                principalTable: "Order",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_OrderDetail_Order_OrderId",
                table: "OrderDetail");

            migrationBuilder.RenameColumn(
                name: "Price",
                table: "OrderDetail",
                newName: "price");

            migrationBuilder.RenameColumn(
                name: "OrderId",
                table: "OrderDetail",
                newName: "orderId");

            migrationBuilder.RenameColumn(
                name: "Id",
                table: "OrderDetail",
                newName: "id");

            migrationBuilder.RenameIndex(
                name: "IX_OrderDetail_OrderId",
                table: "OrderDetail",
                newName: "IX_OrderDetail_orderId");

            migrationBuilder.RenameColumn(
                name: "Surname",
                table: "Order",
                newName: "surname");

            migrationBuilder.RenameColumn(
                name: "Phone",
                table: "Order",
                newName: "phone");

            migrationBuilder.RenameColumn(
                name: "OrderTime",
                table: "Order",
                newName: "orderTime");

            migrationBuilder.RenameColumn(
                name: "Name",
                table: "Order",
                newName: "name");

            migrationBuilder.RenameColumn(
                name: "Email",
                table: "Order",
                newName: "email");

            migrationBuilder.RenameColumn(
                name: "Address",
                table: "Order",
                newName: "address");

            migrationBuilder.RenameColumn(
                name: "Id",
                table: "Order",
                newName: "id");

            migrationBuilder.AlterColumn<string>(
                name: "surname",
                table: "Order",
                type: "nvarchar(max)",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "nvarchar(10)",
                oldMaxLength: 10);

            migrationBuilder.AlterColumn<string>(
                name: "phone",
                table: "Order",
                type: "nvarchar(max)",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "nvarchar(22)",
                oldMaxLength: 22);

            migrationBuilder.AlterColumn<string>(
                name: "name",
                table: "Order",
                type: "nvarchar(max)",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "nvarchar(10)",
                oldMaxLength: 10);

            migrationBuilder.AlterColumn<string>(
                name: "email",
                table: "Order",
                type: "nvarchar(max)",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "nvarchar(30)",
                oldMaxLength: 30);

            migrationBuilder.AlterColumn<string>(
                name: "address",
                table: "Order",
                type: "nvarchar(max)",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "nvarchar(15)",
                oldMaxLength: 15);

            migrationBuilder.AddForeignKey(
                name: "FK_OrderDetail_Order_orderId",
                table: "OrderDetail",
                column: "orderId",
                principalTable: "Order",
                principalColumn: "id",
                onDelete: ReferentialAction.Cascade);
        }
    }
}
