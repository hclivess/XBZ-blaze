import sqlite3
import web
import time

urls = (
    '/', 'index'
)

class index:
    def GET(self):

        # redraw chart
        conn = sqlite3.connect('./ledger.db')
        c = conn.cursor()
        c.execute("SELECT * FROM transactions ORDER BY block_height DESC LIMIT 100;")

        all = c.fetchall()[::-1]

        axis0 = []
        axis1 = []
        axis4 = []
        axis8 = []
        axis9 = []
        axis10 = []

        i = 1
        for x in all:
            axis0.append(x[0])  # append timestamp
            axis1.append(x[1])  # append block height

            axis4.append(x[4])  # append amount
            axis8.append(x[8])  # append fee
            axis9.append(x[9])  # append reward
            axis10.append(x[10])  # append confirmations

        output = "static/plotter.html"
        f = open(output, 'w')

        f.write('<!doctype html>\n')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<title>Line Chart</title>\n')
        f.write('<script src="Chart.js"></script>\n')
        f.write('<link rel="stylesheet" type="text/css" href="style.css">\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('<div style="width:100%">\n')
        f.write('<div>\n')
        # define canvas
        f.write("<h1>Timestamp progression</h1>")
        f.write('<canvas id="canvas" height="150" width="600"></canvas>\n')

        f.write("<h1>Spending in time</h1>")
        f.write('<canvas id="canvas2" height="150" width="600"></canvas>\n')

        f.write("<h1>Fee in time</h1>")
        f.write('<canvas id="canvas3" height="150" width="600"></canvas>\n')

        f.write("<h1>Reward in time</h1>")
        f.write('<canvas id="canvas4" height="150" width="600"></canvas>\n')

        f.write("<h1>Confirmations per block</h1>")
        f.write('<canvas id="canvas5" height="150" width="600"></canvas>\n')
        # define canvas
        f.write('</div>\n')
        f.write('</div>\n')
        f.write('<script>\n')
        f.write('var randomScalingFactor = function(){ return Math.round(Math.random()*100)};\n')

        # onload
        f.write('window.onload = function(){\n')

        f.write('var ctx = document.getElementById("canvas").getContext("2d");\n')
        f.write('window.myLine = new Chart(ctx).Line(lineChartData, {\n')
        f.write('responsive: true\n')
        f.write('});\n')

        f.write('var ctx2 = document.getElementById("canvas2").getContext("2d");\n')
        f.write('window.myLine = new Chart(ctx2).Line(lineChartData2, {\n')
        f.write('responsive: true\n')
        f.write('});\n')

        f.write('var ctx3 = document.getElementById("canvas3").getContext("2d");\n')
        f.write('window.myLine = new Chart(ctx3).Line(lineChartData3, {\n')
        f.write('responsive: true\n')
        f.write('});\n')

        f.write('var ctx4 = document.getElementById("canvas4").getContext("2d");\n')
        f.write('window.myLine = new Chart(ctx4).Line(lineChartData4, {\n')
        f.write('responsive: true\n')
        f.write('});\n')

        f.write('var ctx5 = document.getElementById("canvas5").getContext("2d");\n')
        f.write('window.myLine = new Chart(ctx5).Line(lineChartData5, {\n')
        f.write('responsive: true\n')
        f.write('});\n')

        f.write('}\n')
        # onload

        # segment
        f.write('var lineChartData = {\n')
        f.write('labels : ' + str(map(str, axis0)) + ',\n')
        f.write('datasets : [\n')
        f.write('{\n')
        f.write('label: "My First dataset 1",\n')
        f.write('fillColor : "rgba(220,220,220,0.2)",\n')
        f.write('strokeColor : "rgba(220,220,220,1)",\n')
        f.write('pointColor : "rgba(220,220,220,1)",\n')
        f.write('pointStrokeColor : "#fff",\n')
        f.write('pointHighlightFill : "#fff",\n')
        f.write('pointHighlightStroke : "rgba(220,220,220,1)",\n')
        f.write('data : ' + str(map(str, axis1)) + '\n')
        f.write('}\n')
        f.write(']\n')
        f.write('}\n')

        # segment

        f.write('var lineChartData2 = {\n')
        f.write('labels : ' + str(map(str, axis1)) + ',\n')
        f.write('datasets : [\n')
        f.write('{\n')
        f.write('label: "My First dataset 2",\n')
        f.write('fillColor : "rgba(220,220,220,0.2)",\n')
        f.write('strokeColor : "rgba(220,220,220,1)",\n')
        f.write('pointColor : "rgba(220,220,220,1)",\n')
        f.write('pointStrokeColor : "#fff",\n')
        f.write('pointHighlightFill : "#fff",\n')
        f.write('pointHighlightStroke : "rgba(220,220,220,1)",\n')
        f.write('data : ' + str(map(str, axis4)) + '\n')
        f.write('}\n')
        f.write(']\n')
        f.write('}\n')

        # segment
        f.write('var lineChartData3 = {\n')
        f.write('labels : ' + str(map(str, axis1)) + ',\n')
        f.write('datasets : [\n')
        f.write('{\n')
        f.write('label: "My First dataset 3",\n')
        f.write('fillColor : "rgba(220,220,220,0.2)",\n')
        f.write('strokeColor : "rgba(220,220,220,1)",\n')
        f.write('pointColor : "rgba(220,220,220,1)",\n')
        f.write('pointStrokeColor : "#fff",\n')
        f.write('pointHighlightFill : "#fff",\n')
        f.write('pointHighlightStroke : "rgba(220,220,220,1)",\n')
        f.write('data : ' + str(map(str, axis8)) + '\n')
        f.write('}\n')
        f.write(']\n')
        f.write('}\n')

        # segment
        f.write('var lineChartData4 = {\n')
        f.write('labels : ' + str(map(str, axis1)) + ',\n')
        f.write('datasets : [\n')
        f.write('{\n')
        f.write('label: "My First dataset 4",\n')
        f.write('fillColor : "rgba(220,220,220,0.2)",\n')
        f.write('strokeColor : "rgba(220,220,220,1)",\n')
        f.write('pointColor : "rgba(220,220,220,1)",\n')
        f.write('pointStrokeColor : "#fff",\n')
        f.write('pointHighlightFill : "#fff",\n')
        f.write('pointHighlightStroke : "rgba(220,220,220,1)",\n')
        f.write('data : ' + str(map(str, axis9)) + '\n')
        f.write('}\n')
        f.write(']\n')
        f.write('}\n')

        # segment
        f.write('var lineChartData5 = {\n')
        f.write('labels : ' + str(map(str, axis0)) + ',\n')
        f.write('datasets : [\n')
        f.write('{\n')
        f.write('label: "My First dataset 5",\n')
        f.write('fillColor : "rgba(220,220,220,0.2)",\n')
        f.write('strokeColor : "rgba(220,220,220,1)",\n')
        f.write('pointColor : "rgba(220,220,220,1)",\n')
        f.write('pointStrokeColor : "#fff",\n')
        f.write('pointHighlightFill : "#fff",\n')
        f.write('pointHighlightStroke : "rgba(220,220,220,1)",\n')
        f.write('data : ' + str(map(str, axis10)) + '\n')
        f.write('}\n')
        f.write(']\n')
        f.write('}\n')

        # segment
        f.write('</script>')
        f.write('</body>')
        f.write('</html>')

        f.close()
        # redraw chart

        conn = sqlite3.connect('./ledger.db')
        c = conn.cursor()
        c.execute("SELECT * FROM transactions ORDER BY block_height DESC, timestamp DESC;")

        all = c.fetchall()

        view = []

        for x in all:
            view.append("<tr>")
            view.append("<td>" + str(x[0]) + "</td>")
            view.append("<td>" + str(time.strftime("%Y/%m/%d,%H:%M:%S", time.localtime(float(x[1])))))
            view.append("<td>" + str(x[2]) + "</td>")
            view.append("<td>" + str(x[3].encode('utf-8')) + "</td>")
            view.append("<td>" + str(x[4]) + "</td>")
            #view.append("<td>" + str(x[5]) + "</td>")
            #view.append("<td>" + str(x[6]) + "</td>")
            view.append("<td>" + str(x[7]) + "</td>")
            view.append("<td>" + str(x[8]) + "</td>")
            view.append("<td>" + str(x[9]) + "</td>")
            view.append("<td>" + str(x[10]) + "</td>")
            view.append("<tr>")

        c.close()

        html = "<!DOCTYPE html>" \
               "<html>" \
               "<head>" \
               "<meta http-equiv='refresh' content='60' >" \
               "<link rel='stylesheet' type='text/css' href='static/style.css'>" \
               "</head>" \
               "<META http-equiv='cache-control' content='no-cache'>" \
               "<TITLE>Transaction Explorer</TITLE>" \
               "<body><center><h1>Bismuth Transaction Explorer</h1></center><iframe src='static/plotter.html' width='100%' height='550'></iframe><table style='width:100%'><tr><td>Block</td><td>Timestamp</td><td>From</td><td>To</td><td>Amount</td><td>Transaction Hash</td><td>Fee</td><td>Reward</td><td>Confirmations</td></tr>" + str(
            ''.join(view)) + \
               "</table></body>" \
               "</html>"

        return html

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
