fun main() {
    val n = readLine()!!.toInt()
    var num: Int = 65

    for (i in 0 until n) {
        for (j in 0 until n) {
            print("${num++.toChar()}")
        }
        println()
    }
}