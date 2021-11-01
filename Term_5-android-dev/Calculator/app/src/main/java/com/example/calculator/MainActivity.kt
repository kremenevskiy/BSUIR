package com.example.calculator

import android.content.pm.ActivityInfo
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.SpannableStringBuilder
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.core.content.contentValuesOf
import com.example.calculator.databinding.ActivityMainBinding

import org.mariuszgromada.math.mxparser.*;


class MainActivity : AppCompatActivity() {
    private lateinit var bind: ActivityMainBinding

    var display : TextView? = null;
    var previousCalculations : EditText? = null;

    lateinit var buttonLandscape: Button
    lateinit var buttonPortrait: Button


    class ParseInput(){
        var displayText: String = "0"
        var storedText: String = ""


        fun addNum(addNum: String){
            checkNan()

            if (equalPress) {
                equalPress = false
                displayText = "0"
            }
            if (operator_last) {
                displayText = "0"
            }
            operator_last = false

            val oldStr = displayText
            if (displayText.length > 9){
                return
            }
            if (addNum == ".") {
                if (displayText.contains(".")){
                    return
                }
                displayText = oldStr + addNum
            }
            else if (displayText == "0"){
                displayText = addNum
            }
            else{
                displayText += addNum
            }
        }

        var operator_last = false
        fun operatorPressed(operator: String) {

            if (displayText == "-" && operator == "-"){
                return
            }

            if (powerOfYPressed && operator == "-"){
                addNum("-")
                return
            }

            checkNan()

            Log.d("StartOperator Stored", storedText)
            Log.d("StartOperator Display", displayText)

            if (operator_last && operator != "-"){
                if (storedText.isEmpty()) {
                    return
                }
                if (storedText.last().toString() == operator) {
                    return
                }
                else {
                    storedText = storedText.dropLast(1)
                    storedText += operator
                }
            }

            if (storedText == "" && operator == "-") {
                Log.d("display ", displayText)
                if (displayText == "0") {
                    addNum("-")
                    return
                }
                if (storedText == "") {
                    storedText = displayText + operator
                    displayText = "0"
                    operator_last = true
                }
                return
            }
            else if (storedText == "") {
                storedText = displayText + operator
                displayText = "0"
                operator_last = true
            }
            else {
                if (operator_last && operator == "-") {
                    displayText = "0"
                    addNum("-")
                }
                else {
                    if (!powerOfYPressed){
                        storedText += displayText
                    }
                    displayText = calculate()
                    storedText = displayText + operator
                    operator_last = true
                }
            }

            Log.d("EndOperator Stored", storedText)
            Log.d("EndOperator Display", displayText)

        }

        fun checkNan() {
            if (displayText == "Error") {
                displayText = "0"
            }
        }

        fun checkDivZero() : Boolean {
            val len = storedText.length
            if (len > 2) {
                val lastStr = storedText.subSequence(len - 2, len)
                return lastStr == "/0"
            }
            return true
        }


        fun calculate() : String{


            Log.d("Stored", storedText)
            Log.d("Display", displayText)
            if (checkDivZero()) {
                displayText = "Error"
                storedText = ""
                return "Error"
            }

            if (operator_last) {
                storedText.dropLast(1)
            }

            if (powerOfYPressed) {
                storedText = "$storedText$displayText)"
                powerOfYPressed = false
            }

            if (storedText == ""){
                storedText = displayText
            }

            var userExpr = storedText
            Log.d("Calculate ", storedText)

            userExpr = userExpr.replace("÷", "/")
            userExpr = userExpr.replace("×", "*")

            val exp = Expression(userExpr)
            var result = exp.calculate().toString()

            if (result.toDouble() % 1.0 == 0.0) {
                if (result.toDouble() <= 2147483647) {
                    result = result.toDouble().toInt().toString()
                }
                else {
                    result = result.toDouble().toBigDecimal().toString()
                }
            }

            if (result == "NaN") {
                displayText = "Error"
                storedText = ""
                return "Error"
            }


            displayText = result
            storedText = ""
            Log.d("ResCalculate ", result)
            return result
        }

        var equalPress = false
        fun equalPressed() {
            equalPress = true

            if (!powerOfYPressed) {
                storedText += displayText
            }
            val result = calculate()
            displayText = result
            storedText = ""

        }

        fun removeLast(){
            if (displayText == "Error") {
                displayText = "0"
            }
            if (displayText == "-Infinity"){
                displayText = "0"
            }
            if (displayText == "Infinity"){
                displayText = "0"
            }
            else {
                displayText = displayText.dropLast(1)
            }
        }

        fun clearPressed(){
            displayText = "0"
            storedText = ""
        }

        fun getInput() : String{
            return displayText
        }

        fun scientificPressed(funcStr: String) {
            storedText = "$funcStr$displayText)"
            val result = calculate()
            displayText = result
            storedText = ""
        }

        var ePressed = false
        var piPressed = false
        var powerOfYPressed = false

        fun extraStaffPressed(staff: String) {
            if (staff == "pi"){
                if (!piPressed){
                    displayText = "3.14159265359"
                }
                else {
                    return
                }
            }
            else if(staff == "e"){
                if (!ePressed) {
                    displayText = "2.71828182846"
                }
                else {
                    return
                }
            }
            else if (staff == "^(2)") {
                storedText = displayText + staff
                displayText = calculate()
                storedText = ""
            }
            else if (staff == "^(") {
                storedText = displayText + staff
                powerOfYPressed = true
                displayText = "0"
            }
        }

    }

    var parsing = ParseInput()





    override fun onCreate(savedInstanceState: Bundle?) {



        super.onCreate(savedInstanceState)
        bind = ActivityMainBinding.inflate(layoutInflater)
        val view = bind.root
        setContentView(view)



        bind.displayEditText.setText("0")




        bind.buttonSetLandscape?.setOnClickListener {
            requestedOrientation = ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE
            Toast.makeText(baseContext, "Landscape Orientation", Toast.LENGTH_SHORT).show()
        }
        bind.buttonSetPortrait?.setOnClickListener {
            requestedOrientation = ActivityInfo.SCREEN_ORIENTATION_PORTRAIT
            Toast.makeText(baseContext, "Portrait Orientation", Toast.LENGTH_SHORT).show()
        }

//        setContentView(R.layout.activity_main)

//        display = findViewById<TextView>(R.id.displayEditText);
//        bind.displayEditText.setText("3w424");
//        previousCalculations = Text

        bind.displayEditText.showSoftInputOnFocus = false

    }

    private fun updateText(strToAdd : String){
//        display?.setText(strToAdd);
//        bind.displayEditText.setText(strToAdd)

        val oldStr = bind.displayEditText.text
        val cursorPos = bind.displayEditText.selectionStart;

        val leftStr = oldStr.substring(0, cursorPos)
        val rightStr = oldStr.substring(cursorPos)

        bind.displayEditText.setText(String.format("%s%s%s", leftStr, strToAdd, rightStr))
        bind.displayEditText.setSelection(cursorPos + strToAdd.length)
    }

    public fun zeroBTNPush(view : View){
        parsing.addNum("0")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun oneBTNPush(view : View){
        parsing.addNum("1")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun twoBTNPush(view : View){
        parsing.addNum("2")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun threeBTNPush(view : View){
        parsing.addNum("3")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun fourBTNPush(view : View){
        parsing.addNum("4")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun fiveBTNPush(view : View){
        parsing.addNum("5")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun sixBTNPush(view : View){
        parsing.addNum("6")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun sevenBTNPush(view : View){
        parsing.addNum("7")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun eightBTNPush(view : View){
        parsing.addNum("8")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun nineBTNPush(view : View){
        parsing.addNum("9")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun addBTNPush(view : View){
        parsing.operatorPressed("+")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun subtractBTNPush(view : View){
        parsing.operatorPressed("-")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun multiplyBTNPush(view : View){
        parsing.operatorPressed("*")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun divBTNPush(view : View){
        parsing.operatorPressed("/")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun dotBTNPush(view : View){
        parsing.addNum(".")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun rightParentBTNPush(view : View){
        updateText(resources.getString(R.string.parenthesesOpenText));
    }
    public fun leftParentBTNPush(view : View){
        updateText(resources.getString(R.string.parenthesesCloseText));
    }
    public fun clearBTNPush(view : View){
        parsing.clearPressed()
        bind.displayEditText.setText(parsing.getInput())
        bind.previousCalculationView.setText("")
    }
    public fun backspaceBTNPush(view : View){
        parsing.removeLast()
        bind.displayEditText.setText(parsing.getInput())
//        val cursorPos = bind.displayEditText.selectionStart;
//        val textLen = bind.displayEditText.text.length

//        if (cursorPos != 0 && textLen != 0 ) {
//
//            val selection = bind.displayEditText.text as SpannableStringBuilder;
//            selection.replace(cursorPos-1, cursorPos, "")
//            bind.displayEditText.text = selection;
//            bind.displayEditText.setSelection(cursorPos-1)
//        }
    }
    public fun equalBTNPush(view : View){
        parsing.equalPressed()
        bind.displayEditText.setText(parsing.displayText)
//        var userExpr = bind.displayEditText.text.toString()
//
//        bind.previousCalculationView.text = userExpr
//
//        userExpr = userExpr.replace(resources.getString(R.string.divideText), "/")
//        userExpr = userExpr.replace(resources.getString(R.string.multiplyText), "*")
//
//        val exp = Expression(userExpr)
//        val result = exp.calculate().toString()
//        bind.displayEditText.setText(result)
//        bind.displayEditText.setSelection(result.length)
    }

    public fun trigSinBTNPush(view : View){
        parsing.scientificPressed("sin(")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun trigCosBTNPush(view : View){
        parsing.scientificPressed("cos(")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun trigTanBTNPush(view : View){
        parsing.scientificPressed("tan(")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun trigArcSinBTNPush(view : View){
        parsing.scientificPressed("arcsin(")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun trigArcCosBTNPush(view : View){
        parsing.scientificPressed("arccos(")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun trigArcTanBTNPush(view : View){
        parsing.scientificPressed("arctan(")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun logBTNPush(view : View){
        parsing.scientificPressed("log2(")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun naturalLogBTNPush(view : View){
        parsing.scientificPressed("ln(")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun squareRootTNPush(view : View){
        parsing.scientificPressed("sqrt(")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun eBTNPush(view : View){
        parsing.extraStaffPressed("e")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun piBTNPush(view : View){
        parsing.extraStaffPressed("pi")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun absoluteValueBTNPush(view : View){
        parsing.scientificPressed("abs(")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun isPrimeBTNPush(view : View){
        parsing.scientificPressed("ispr(")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun xSquaredBTNPush(view : View){
        parsing.extraStaffPressed("^(2)")
        bind.displayEditText.setText(parsing.getInput())
    }
    public fun xPowerYBTNPush(view : View){
        parsing.extraStaffPressed("^(")
        bind.displayEditText.setText(parsing.getInput())
    }
}

