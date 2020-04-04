import ScriptEnv
def simulate(Position, Phase, Current):
    for i in range(len(Position)):
        ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
        oDesktop.RestoreWindow()
        oProject = oDesktop.SetActiveProject("BshieldX")
        oDesign = oProject.SetActiveDesign("Maxwell3DDesign1")
        oDesign.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:LocalVariableTab",
                    [
                        "NAME:PropServers",
                        "LocalVariables"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:SHY",
                            "Value:=", Position[i]
                        ]
                    ]
                ]
            ])
        oModule = oDesign.GetModule("BoundarySetup")
        oModule.EditCurrent("3",
                            [
                                "NAME:3",
                                "Phase:=", Phase[i] + 'deg',
                                "Current:=", '(' + Current[i] + ') A',
                                "IsSolid:=", False,
                                "Point out of terminal:=", False
                            ])
        oProject.Save()
        oDesign.AnalyzeAll()
        oModule = oDesign.GetModule("ReportSetup")
        oModule.CreateReport("Data Table 1", "Fields", "Data Table", "Setup1 : LastAdaptive", [],
                             [
                                 "Freq:=", ["All"],
                                 "Phase:=", ["0deg"],
                                 "Ns:=", ["Nominal"],
                                 "Np:=", ["Nominal"],
                                 "H:=", ["Nominal"],
                                 "Nsh:=", ["Nominal"],
                                 "Nm:=", ["Nominal"],
                                 "MOVY:=", ["Nominal"],
                                 "MOVX:=", ["Nominal"],
                                 "MOVZ:=", ["Nominal"],
                                 "SHY:=", ["Nominal"]
                             ],
                             [
                                 "X Component:=", "Freq",
                                 "Y Component:=", ["B_AVE"]
                             ], [])
        oModule.ExportToFile("Data Table 1",
                             "E:/outputData{}_position_{}.csv".format(str(i + 1), Position[i]))
        oModule.DeleteReports(["Data Table 1"])
        oDesign.DeleteFullVariation("All", False)
        oProject.Save()


def main():
	Position = ['300mm', '350mm', '400mm', '450mm', '500mm', '550mm', '600mm', '650mm']
	Phase = ['-18.58', '-25.36', '-28.5', '-30.11', '-30.49', '-30.53', '-30.52', '-30.57']
	Current = ['29.58*5', '18.7*5', '13.27*5', '8.55*5', '5.83*5', '4.44*5', '3.21*5', '2.39*5']
	simulate(Position, Phase, Current)


if __name__ == '__main__':
    main()
