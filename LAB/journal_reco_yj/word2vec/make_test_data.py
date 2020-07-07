import csv

f = open('test_input_elsevier.csv', 'w', encoding='utf-8')
wr = csv.writer(f)

at1 = "Wirtinger-based integral inequality: Application to time-delay systems"
at1 = at1.replace(","," ")
aa1 = "In the last decade, the Jensen inequality has been intensively used in the context of time-delay or sampled-data systems since it is an appropriate tool to derive tractable stability conditions expressed in terms of linear matrix inequalities (LMIs). However, it is also well-known that this inequality introduces an undesirable conservatism in the stability conditions and looking at the literature, reducing this gap is a relevant issue and always an open problem. In this paper, we propose an alternative inequality based on the Fourier Theory, more precisely on the Wirtinger inequalities. It is shown that this resulting inequality encompasses the Jensen one and also leads to tractable LMI conditions. In order to illustrate the potential gain of employing this new inequality with respect to the Jensen one, two applications on time-delay and sampled-data stability analysis are provided. © 2013 Elsevier Ltd. All rights reserved."
aa1 = aa1.replace(","," ")
ak1 = "Jensen inequality, Sampled-data systems, Stability analysis, Time-delay systems"
ak1 = ak1.replace(","," ")
a1 = at1+" "+aa1+" "+ak1
la1 = [at1, aa1, ak1, a1, "Automatica"]

at2 = "3D, SF and the future"
at2 = at2.replace(","," ")
aa2 = "This article assesses the use of 'science fiction' (SF) in visioning or prototyping the potential economic and social consequences of so-called 3D printing. What is becoming clear to many commentators as well as science fiction writers is how rapid prototyping, or 3D printing more generally, could permit many final objects to be made near to or even by consumers on just-in-time 'printing' machines. This revolution in making would have many implications for the economy-and-society in the future by seriously augmenting, or possibly replacing, current systems of manufactured production, long-distance transportation and consumption. These 3D technologies have featured in SF works, including Neal Stephenson's The Diamond Age, Ian McDonald's Brasyl, Charles Stross's Rule 34 and Cory Doctorow's Makers. The article reports on current research seeking to understand the implications of what may be a major new sociotechnical system in the making. Some creative uses of SF are presented in a professional workshop setting. As well the article documents the use of SF as a methodological prototype in forecasting alternative scenarios of the future. SF prototyping could be a powerful tool in the social science repertoire when put into action in forecasting possible technology and business futures."
aa2 = aa2.replace(","," ")
ak2 = "business, consumption behavior, forecasting method, future prospect, manufacturing, technology, transportation"
ak2 = ak2.replace(","," ")
a2 = at2+" "+aa2+" "+ak2
la2 = [at2,aa2,ak2,a2, "Futures"]

at3 = "Rings and modules which are stable under automorphisms of their injective hulls"
at3 = at3.replace(","," ")
aa3 = "It is proved, among other results, that a prime right nonsingular ring (in particular, a simple ring) R is right self-injective if R R is invariant under automorphisms of its injective hull. This answers two questions raised by Singh and Srivastava, and Clark and Huynh. An example is given to show that this conclusion no longer holds when prime ring is replaced by semiprime ring in the above assumption. Also shown is that automorphism-invariant modules are precisely pseudo-injective modules, answering a recent question of Lee and Zhou. Furthermore, rings whose cyclic modules are automorphism-invariant are investigated."
aa3 = aa3.replace(","," ")
ak3 = "Automorphism-invariant, Prime self-injective ring, Pseudo-injective, Quasi-injective module"
ak3 = ak3.replace(","," ")
a3 = at3+" "+aa3+" "+ak3
la3 = [at3,aa3,ak3,a3, "Journal of Algebra"]

at4 = "Characterization of copper species over Cu/SAPO-34 in selective catalytic reduction of NOx with ammonia: Relationships between active Cu sites and de-NOx performance at low temperature"
at4 = at4.replace(","," ")
aa4 = "To investigate the active Cu sites in the selective catalytic reduction of NO by NH3 (NH3 SCR) over Cu/SAPO-34 catalysts, a series of samples containing different Cu loadings has been prepared by an ion-exchange process. A combination of H2 TPR and EPR techniques was applied to identify and quantify the isolated Cu2+ sites. The trend of the isolated Cu2+ ions in the samples estimated by EPR is similar to that from TPR results and was found to be proportional to the NH3 SCR reaction rates. The turnover frequency (TOF) calculated based on the number of isolated Cu2+ ions on samples with varying Cu loadings showed a constant value at the same temperature. Thus, we conclude that the isolated Cu2+ species associated with the six-ring window and displaced into the ellipsoidal cavity of SAPO-34 (Site (I)) are the active sites for the NH3 SCR reaction in the temperature range 100-200 °C."
aa4 = aa4.replace(","," ")
ak4 = "Active sites, Cu/SAPO-34, Isolated Cu2+, NH3 SCR, Reaction rate, TOF"
ak4 = ak4.replace(","," ")
a4 = at4+" "+aa4+" "+ak4
la4 = [at4,aa4,ak4,a4, "Journal of Catalysis"]

at5 = "Comparison of the ARMA, ARIMA, and the autoregressive artificial neural network models in forecasting the monthly inflow of Dez dam reservoir"
at5 = at5.replace(","," ")
aa5 = "The goal of the present research is forecasting the inflow of Dez dam reservoir by using Auto Regressive Moving Average (ARMA) and Auto Regressive Integrated Moving Average (ARIMA) models while increasing the number of parameters in order to increase the forecast accuracy to four parameters and comparing them with the static and dynamic artificial neural networks. In this research, monthly discharges from 1960 to 2007 were used. The statistics related to first 42. years were used to train the models and the 5 past years were used to forecast. In ARMA and ARIMA models, the polynomial was derived respectively with four and six parameters to forecast the inflow. In the artificial neural network, the radial and sigmoid activity functions were used with several different neurons in the hidden layers. By comparing root mean square error (RMSE) and mean bias error (MBE), dynamic artificial neural network model with sigmoid activity function and 17 neurons in the hidden layer was chosen as the best model for forecasting inflow of the Dez dam reservoir. Inflow of the dam reservoir in the 12 past months shows that ARIMA model had a less error compared with the ARMA model. Static and Dynamic autoregressive artificial neural networks with activity sigmoid function can forecast the inflow to the dam reservoirs from the past 60. months."
aa5 = aa5.replace(","," ")
ak5 = "ARIMA, ARMA, Autoregressive artificial neural network, Dez dam, Forecast of dam reservoir inflow"
ak5 = ak5.replace(","," ")
a5 = at5+" "+aa5+" "+ak5
la5 = [at5, aa5,ak5,a5, "Journal of Hydrology"]


wr.writerow(la1)
wr.writerow(la2)
wr.writerow(la3)
wr.writerow(la4)
wr.writerow(la5)

f.close()