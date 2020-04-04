import ScriptEnv


def simulate(Position, Phase, Current):
    ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
    oDesktop.RestoreWindow()
    oProject = oDesktop.SetActiveProject("BshieldX")
    oDesign = oProject.SetActiveDesign("Maxwell3DDesign1")
    # oDesign.DeleteFullVariation("All", False)
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
                        "Value:=", Position
                    ]
                ]
            ]
        ])
    oModule = oDesign.GetModule("BoundarySetup")
    oModule.EditCurrent("3",
                        [
                            "NAME:3",
                            "Phase:=", Phase + 'deg',
                            "Current:=", '(' + Current + ') A',
                            "IsSolid:=", False,
                            "Point out of terminal:=", False
                        ])
    oProject.Save()
    oDesign.AnalyzeAll()
    # oModule = oDesign.GetModule("ReportSetup")
    # oModule.CreateReport("Data Table 1", "Fields", "Data Table", "Setup1 : LastAdaptive", [],
    #                      [
    #                          "Freq:=", ["All"],
    #                          "Phase:=", ["0deg"],
    #                          "Ns:=", ["Nominal"],
    #                          "Np:=", ["Nominal"],
    #                          "H:=", ["Nominal"],
    #                          "Nsh:=", ["Nominal"],
    #                          "Nm:=", ["Nominal"],
    #                          "MOVY:=", ["Nominal"],
    #                          "MOVX:=", ["Nominal"],
    #                          "MOVZ:=", ["Nominal"],
    #                          "SHY:=", ["Nominal"]
    #                      ],
    #                      [
    #                          "X Component:=", "Freq",
    #                          "Y Component:=", ["B_AVE"]
    #                      ], [])
    # oModule.ExportToFile("Data Table 1",
    #                      "E:/outputData_position_{}.csv".format(Position))
    # oModule.DeleteReports(["Data Table 1"])
    oModule = oDesign.GetModule("FieldsReporter")
    oModule.CreateFieldPlot(
        [
            "NAME:ComplexMag_B1",
            "SolutionName:=", "Setup1 : LastAdaptive",
            "QuantityName:=", "ComplexMag_B",
            "PlotFolder:=", "B",
            "UserSpecifyName:=", 0,
            "UserSpecifyFolder:=", 0,
            "StreamlinePlot:=", False,
            "IntrinsicVar:=", "Freq=\'85kHz\' Phase=\'0deg\'",
            "PlotGeomInfo:=", [1, "Surface", "CutPlane", 1, "Global:YZ"],
            "FilterBoxes:=", [1, ""],
            [
                "NAME:PlotOnSurfaceSettings",
                "Filled:=", False,
                "IsoValType:=", "Fringe",
                "SmoothShade:=", True,
                "AddGrid:=", False,
                "MapTransparency:=", True,
                "Refinement:=", 0,
                "Transparency:=", 0,
                [
                    "NAME:Arrow3DSpacingSettings",
                    "ArrowUniform:=", True,
                    "ArrowSpacing:=", 0,
                    "MinArrowSpacing:=", 0,
                    "MaxArrowSpacing:=", 0
                ],
                "GridColor:=", [255, 255, 255]
            ]
        ])
    oModule.SetPlotFolderSettings("B",
                                  [
                                      "NAME:FieldsPlotSettings",
                                      "Real time mode:=", True,
                                      [
                                          "NAME:ColorMapSettings",
                                          "ColorMapType:=", "Spectrum",
                                          "SpectrumType:=", "Rainbow",
                                          "UniformColor:=", [127, 255, 255],
                                          "RampColor:=", [255, 127, 127]
                                      ],
                                      [
                                          "NAME:Scale3DSettings",
                                          "unit:=", 103,
                                          "m_nLevels:=", 15,
                                          "minvalue:=", 9.1261E-11,
                                          "maxvalue:=", 0.01641,
                                          "log:=", False,
                                          "IntrinsicMin:=", 9.12614567250003E-11,
                                          "IntrinsicMax:=", 0.0164098460227251,
                                          "LimitFieldValuePrecision:=", False,
                                          "FieldValuePrecisionDigits:=", 4,
                                          "dB:=", False,
                                          "ScaleType:=", 1,
                                          "UserSpecifyValues:=",
                                          [16, 9.12609987580026E-11, 0.00109400018118322, 0.00218800012953579
                                              , 0.00328200031071901, 0.00437600025907159, 0.00547000020742416
                                              , 0.00656400062143803, 0.0076580005697906, 0.00875200051814318
                                              , 0.00984600093215704, 0.0109400004148483, 0.0120340008288622
                                              , 0.0131280012428761, 0.0142220007255673, 0.0153160011395812
                                              , 0.0164100006222725],
                                          "ValueNumberFormatTypeAuto:=", 1,
                                          "ValueNumberFormatTypeScientific:=", True,
                                          "ValueNumberFormatWidth:=", 12,
                                          "ValueNumberFormatPrecision:=", 4
                                      ],
                                      [
                                          "NAME:Marker3DSettings",
                                          "MarkerType:=", 9,
                                          "MarkerMapSize:=", True,
                                          "MarkerMapColor:=", False,
                                          "MarkerSize:=", 0.25
                                      ],
                                      [
                                          "NAME:Arrow3DSettings",
                                          "ArrowType:=", 1,
                                          "ArrowMapSize:=", True,
                                          "ArrowMapColor:=", True,
                                          "ShowArrowTail:=", True,
                                          "ArrowSize:=", 0.25,
                                          "ArrowMinMagnitude:=", -0.499999999908739,
                                          "ArrowMaxMagnitude:=", 0.516409846022725,
                                          "ArrowMagnitudeThreshold:=", 0,
                                          "ArrowMagnitudeFilteringFlag:=", False,
                                          "ArrowMinIntrinsicMagnitude:=", 0,
                                          "ArrowMaxIntrinsicMagnitude:=", 1
                                      ],
                                      [
                                          "NAME:DeformScaleSettings",
                                          "ShowDeformation:=", True,
                                          "MinScaleFactor:=", 0,
                                          "MaxScaleFactor:=", 1,
                                          "DeformationScale:=", 0
                                      ]
                                  ])
    oModule.SetPlotFolderSettings("B",
                                  [
                                      "NAME:FieldsPlotSettings",
                                      "Real time mode:=", True,
                                      [
                                          "NAME:ColorMapSettings",
                                          "ColorMapType:=", "Spectrum",
                                          "SpectrumType:=", "Rainbow",
                                          "UniformColor:=", [127, 255, 255],
                                          "RampColor:=", [255, 127, 127]
                                      ],
                                      [
                                          "NAME:Scale3DSettings",
                                          "unit:=", 104,
                                          "m_nLevels:=", 15,
                                          "minvalue:=", 9.1261E-11,
                                          "maxvalue:=", 0.01641,
                                          "log:=", False,
                                          "IntrinsicMin:=", 9.12614567250003E-11,
                                          "IntrinsicMax:=", 0.0164098460227251,
                                          "LimitFieldValuePrecision:=", False,
                                          "FieldValuePrecisionDigits:=", 4,
                                          "dB:=", False,
                                          "ScaleType:=", 1,
                                          "UserSpecifyValues:=",
                                          [16, 9.12609987580026E-11, 0.00109400018118322, 0.00218800012953579
                                              , 0.00328200031071901, 0.00437600025907159, 0.00547000020742416
                                              , 0.00656400062143803, 0.0076580005697906, 0.00875200051814318
                                              , 0.00984600093215704, 0.0109400004148483, 0.0120340008288622
                                              , 0.0131280012428761, 0.0142220007255673, 0.0153160011395812
                                              , 0.0164100006222725],
                                          "ValueNumberFormatTypeAuto:=", 1,
                                          "ValueNumberFormatTypeScientific:=", True,
                                          "ValueNumberFormatWidth:=", 12,
                                          "ValueNumberFormatPrecision:=", 4
                                      ],
                                      [
                                          "NAME:Marker3DSettings",
                                          "MarkerType:=", 9,
                                          "MarkerMapSize:=", True,
                                          "MarkerMapColor:=", False,
                                          "MarkerSize:=", 0.25
                                      ],
                                      [
                                          "NAME:Arrow3DSettings",
                                          "ArrowType:=", 1,
                                          "ArrowMapSize:=", True,
                                          "ArrowMapColor:=", True,
                                          "ShowArrowTail:=", True,
                                          "ArrowSize:=", 0.25,
                                          "ArrowMinMagnitude:=", -0.499999999908739,
                                          "ArrowMaxMagnitude:=", 0.516409846022725,
                                          "ArrowMagnitudeThreshold:=", 0,
                                          "ArrowMagnitudeFilteringFlag:=", False,
                                          "ArrowMinIntrinsicMagnitude:=", 0,
                                          "ArrowMaxIntrinsicMagnitude:=", 1
                                      ],
                                      [
                                          "NAME:DeformScaleSettings",
                                          "ShowDeformation:=", True,
                                          "MinScaleFactor:=", 0,
                                          "MaxScaleFactor:=", 1,
                                          "DeformationScale:=", 0
                                      ]
                                  ])
    oModule.SetPlotFolderSettings("B",
                                  [
                                      "NAME:FieldsPlotSettings",
                                      "Real time mode:=", True,
                                      [
                                          "NAME:ColorMapSettings",
                                          "ColorMapType:=", "Spectrum",
                                          "SpectrumType:=", "Rainbow",
                                          "UniformColor:=", [127, 255, 255],
                                          "RampColor:=", [255, 127, 127]
                                      ],
                                      [
                                          "NAME:Scale3DSettings",
                                          "unit:=", 104,
                                          "m_nLevels:=", 15,
                                          "minvalue:=", 0,
                                          "maxvalue:=", 0.01641,
                                          "log:=", False,
                                          "IntrinsicMin:=", 9.12614567250003E-11,
                                          "IntrinsicMax:=", 0.0164098460227251,
                                          "LimitFieldValuePrecision:=", False,
                                          "FieldValuePrecisionDigits:=", 4,
                                          "dB:=", False,
                                          "ScaleType:=", 1,
                                          "UserSpecifyValues:=",
                                          [16, 9.12609987580026E-11, 0.00109400018118322, 0.00218800012953579
                                              , 0.00328200031071901, 0.00437600025907159, 0.00547000020742416
                                              , 0.00656400062143803, 0.0076580005697906, 0.00875200051814318
                                              , 0.00984600093215704, 0.0109400004148483, 0.0120340008288622
                                              , 0.0131280012428761, 0.0142220007255673, 0.0153160011395812
                                              , 0.0164100006222725],
                                          "ValueNumberFormatTypeAuto:=", 1,
                                          "ValueNumberFormatTypeScientific:=", True,
                                          "ValueNumberFormatWidth:=", 12,
                                          "ValueNumberFormatPrecision:=", 4
                                      ],
                                      [
                                          "NAME:Marker3DSettings",
                                          "MarkerType:=", 9,
                                          "MarkerMapSize:=", True,
                                          "MarkerMapColor:=", False,
                                          "MarkerSize:=", 0.25
                                      ],
                                      [
                                          "NAME:Arrow3DSettings",
                                          "ArrowType:=", 1,
                                          "ArrowMapSize:=", True,
                                          "ArrowMapColor:=", True,
                                          "ShowArrowTail:=", True,
                                          "ArrowSize:=", 0.25,
                                          "ArrowMinMagnitude:=", -0.499999999908739,
                                          "ArrowMaxMagnitude:=", 0.516409846022725,
                                          "ArrowMagnitudeThreshold:=", 0,
                                          "ArrowMagnitudeFilteringFlag:=", False,
                                          "ArrowMinIntrinsicMagnitude:=", 0,
                                          "ArrowMaxIntrinsicMagnitude:=", 1
                                      ],
                                      [
                                          "NAME:DeformScaleSettings",
                                          "ShowDeformation:=", True,
                                          "MinScaleFactor:=", 0,
                                          "MaxScaleFactor:=", 1,
                                          "DeformationScale:=", 0
                                      ]
                                  ])
    oModule.SetPlotFolderSettings("B",
                                  [
                                      "NAME:FieldsPlotSettings",
                                      "Real time mode:=", True,
                                      [
                                          "NAME:ColorMapSettings",
                                          "ColorMapType:=", "Spectrum",
                                          "SpectrumType:=", "Rainbow",
                                          "UniformColor:=", [127, 255, 255],
                                          "RampColor:=", [255, 127, 127]
                                      ],
                                      [
                                          "NAME:Scale3DSettings",
                                          "unit:=", 104,
                                          "m_nLevels:=", 15,
                                          "minvalue:=", 0,
                                          "maxvalue:=", 2.7E-05,
                                          "log:=", False,
                                          "IntrinsicMin:=", 9.12614567250003E-11,
                                          "IntrinsicMax:=", 0.0164098460227251,
                                          "LimitFieldValuePrecision:=", False,
                                          "FieldValuePrecisionDigits:=", 4,
                                          "dB:=", False,
                                          "ScaleType:=", 1,
                                          "UserSpecifyValues:=",
                                          [16, 9.12609987580026E-11, 0.00109400018118322, 0.00218800012953579
                                              , 0.00328200031071901, 0.00437600025907159, 0.00547000020742416
                                              , 0.00656400062143803, 0.0076580005697906, 0.00875200051814318
                                              , 0.00984600093215704, 0.0109400004148483, 0.0120340008288622
                                              , 0.0131280012428761, 0.0142220007255673, 0.0153160011395812
                                              , 0.0164100006222725],
                                          "ValueNumberFormatTypeAuto:=", 1,
                                          "ValueNumberFormatTypeScientific:=", True,
                                          "ValueNumberFormatWidth:=", 12,
                                          "ValueNumberFormatPrecision:=", 4
                                      ],
                                      [
                                          "NAME:Marker3DSettings",
                                          "MarkerType:=", 9,
                                          "MarkerMapSize:=", True,
                                          "MarkerMapColor:=", False,
                                          "MarkerSize:=", 0.25
                                      ],
                                      [
                                          "NAME:Arrow3DSettings",
                                          "ArrowType:=", 1,
                                          "ArrowMapSize:=", True,
                                          "ArrowMapColor:=", True,
                                          "ShowArrowTail:=", True,
                                          "ArrowSize:=", 0.25,
                                          "ArrowMinMagnitude:=", -0.499999999908739,
                                          "ArrowMaxMagnitude:=", 0.516409846022725,
                                          "ArrowMagnitudeThreshold:=", 0,
                                          "ArrowMagnitudeFilteringFlag:=", False,
                                          "ArrowMinIntrinsicMagnitude:=", 0,
                                          "ArrowMaxIntrinsicMagnitude:=", 1
                                      ],
                                      [
                                          "NAME:DeformScaleSettings",
                                          "ShowDeformation:=", True,
                                          "MinScaleFactor:=", 0,
                                          "MaxScaleFactor:=", 1,
                                          "DeformationScale:=", 0
                                      ]
                                  ])
    oProject.Save()


def main():
    '''
    300mm:0, 350mm:1,400mm:2,450mm:3,500mm:4, 550mm:5,600mm:6,650mm:7
    '''
    i = 8
    Position = ['300mm', '350mm', '400mm', '450mm', '500mm', '550mm', '600mm', '650mm', '650mm']
    Phase = ['-18.58', '-25.36', '-28.5', '-30.11', '-30.49', '-30.53', '-30.52', '-30.57', '0']
    Current = ['29.58*5', '18.7*5', '13.27*5', '8.55*5', '5.83*5', '4.44*5', '3.21*5', '2.39*5', '0']
    simulate(Position[i], Phase[i], Current[i])


if __name__ == '__main__':
    main()
