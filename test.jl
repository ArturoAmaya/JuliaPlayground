using CurricularAnalytics, CurricularVisualization

curr = read_csv("./NEWCURR1.csv")
visualize(curr)

curr2 = Curriculum("Curr2", curr.courses)