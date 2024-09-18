fun main() {
    var num: Int = 0
    val n: Int = readLine()!!.toInt()
    for (i in 1 .. n) {
        for (j in 1..i) {
            print("${(num++ + 65).toChar()}")
            num %= 26
        }
        println()
    }
}