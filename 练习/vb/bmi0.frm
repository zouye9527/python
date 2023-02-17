VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "身高体重指数BMI计算"
   ClientHeight    =   3510
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   7425
   LinkTopic       =   "Form1"
   ScaleHeight     =   3510
   ScaleWidth      =   7425
   StartUpPosition =   3  '窗口缺省
   Begin VB.CommandButton Command2 
      Caption         =   "退出"
      Height          =   495
      Left            =   4440
      TabIndex        =   6
      Top             =   2160
      Width           =   1695
   End
   Begin VB.CommandButton Command1 
      Caption         =   "计算BMI"
      Height          =   495
      Left            =   1920
      TabIndex        =   5
      Top             =   2160
      Width           =   1455
   End
   Begin VB.TextBox Text2 
      Height          =   495
      Left            =   1320
      TabIndex        =   3
      Top             =   1200
      Width           =   1695
   End
   Begin VB.TextBox Text1 
      Height          =   495
      Left            =   1320
      TabIndex        =   2
      Top             =   480
      Width           =   1695
   End
   Begin VB.Label Label3 
      Height          =   735
      Left            =   3960
      TabIndex        =   4
      Top             =   600
      Width           =   3135
   End
   Begin VB.Label Label2 
      Alignment       =   2  'Center
      Caption         =   "体重kg"
      Height          =   255
      Left            =   360
      TabIndex        =   1
      Top             =   1200
      Width           =   615
   End
   Begin VB.Label Label1 
      Alignment       =   2  'Center
      Caption         =   "身高cm"
      Height          =   255
      Left            =   360
      TabIndex        =   0
      Top             =   600
      Width           =   735
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
Dim sg As Double  '身高
Dim tz As Double  '体重
Dim jg As Double  '结果

sg = Val(Text1)
tz = Val(Text2)
jg = tz / ((sg / 100) ^ 2)

Select Case jg

Case ls < 18.5
Label3.Caption = "您的BMI值结果为：" & Format(jg, "00.00") & vbCrLf & "过轻，请合理添加膳食，补充营养！"
Case 18.5 To 23.9
Label3.Caption = "您的BMI值结果为：" & Format(jg, "00.00") & vbCrLf & "正常，请注意保持！"
Case 24 To 27
Label3.Caption = "您的BMI值结果为：" & Format(jg, "00.00") & vbCrLf & "重了，请注意！"
Case 28 To 32
Label3.Caption = "您的BMI值结果为：" & Format(jg, "00.00") & vbCrLf & "胖了，请多加运动，保持身体健康！"
Case ls > 32
Label3.Caption = "您的BMI值结果为：" & Format(jg, "00.00") & vbCrLf & "喝水都胖，我也很无奈！"

End Select
End Sub

Private Sub Command2_Click()
End
End Sub
