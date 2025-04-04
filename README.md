# Inside The Neutron: Extracting Neutron Form-Factors in Deuteron Electrodisintegration Processes

We investigate the extraction of neutron form-factors in high Q<sup>2</sup> exclusive deuteron electrodisintegration processes to understand the internal structure of the neutron. Form-Factors are a quantitative value that describes the distribution of charge (G<sub>E</sub>) and magnetization (G<sub>M</sub>) within the neutron and also aids in understanding the quark-gluon composition. We investigate kinematics that minimize nuclear effects to obtain precise measurements.

## Reaction

The main concern when trying to extract the neutron form-factors is the lack of a free neutron target. To reliably isolate the neutron contribution, scattering from atomic nuclei is required.

We compute the kinematics of the following quasi-elastic scattering process:

<p align="center"><b><i>e + d → e' + N<sub>f</sub> + N<sub>r</sub></i></b></p>

An electron beam hits a stationary deuteron (deuterium nucleus) target and results in a scattered electron, a knock-out nucleon, and recoil nucleon. We investigate the process of the detected knock-out nucleon being the neutron and the recoil nucleon being the proton.

## Re-scatterings

We consider three main contributions when analyzing the reaction's cross-section (production rate or probability of a specific interaction occurring):

<p align = "center" href="url"><img src="https://github.com/MarlenAnalytics/deuteron_electrodisintegration/blob/main/diagrams_edepn.png" height="300" width="500" ></p>


(a) `Plane Wave Impulse Approximation (PWIA)` The incoming particle is assumed to be a plane wave, meaning its wave function is uniform in space and only varies in time and direction. This assumption simplifies the description of the incoming wave as it doesn't account for any potential distortions or interactions with the medium before the scattering event.
This also assumes that the interaction between the incoming particle and the deuteron is localized, meaning that the nucleus is treated as if it is made of individual nucleons, each of which interacts independently with the incoming particle. The nucleus is seen as a collection of 'free nucleons', with no other nuclear effects taken into account during the scattering process.

(b) `Final State Interaction (FSI)` refers to the interactions that occur between the particles in the final state of a scattering process after the initial interaction has taken place. After the electron interacts with the deuteron, the proton and neutron in the final state may still interact with each other.

(c) `Charge Exchange (CHEX)` refers to the re-scattering process in the final state where there is a transfer of charge between the proton and neutron. Whilst the cause is still unknown, this results in the proton becoming a neutron, and the neutron becoming a proton which can heavily affect the cross-section.

(d) `Resonance` is the excitation of nucleons to higher energy states. In our case, this contribution can be neglected.


## Variables and Parameters

The computation of the kinematics is performed separately in GFortran and can not be shared as it is private information, but the following list defines some of the variables and parameters used to conduct the analysis and visualizations.

- `Q²` (Q-squared) represents the four-momentum transfer squared in a scattering process. It is significant for analyzing how the virtual photon interacts with the neutron inside the deuteron and how nuclear effects influence the cross-section.

- `Pᵣ` Recoil nucleon (proton) momenta.

- `Recoil Nucleon Polar Angle (θᵣ)` Recoil nucleon production with respect to the virtual photon (q).

- `θ_pq` Polar angle of struck nucleon with respect to q.

- `x_B` Bjorken Scaling refers to a dimensionless scaling unit that suggests that experimentally observed strongly interacting particles behave as collections of point-like constituents when probed at high energies.
  

## Analysis

### Stationary, Moving, and Bound

<p align = "center" href="url"><img src="https://github.com/MarlenAnalytics/deuteron_electrodisintegration/blob/main/crs_vs_thr0.png" height="400" width="550" ></p>

The above visualization depicts the calculated cross-section values plotted with respect to the recoil nucleon polar angle at various recoil nucleon momenta with Q<sup>2</sup> set to 4.0 GeV. The stationary and moving cross-section curves assumes that the neutron is hypothetically 'free'. Whilst the bound cross-section curves takes into account the binding effects of the neutron being bound within the deuteron. Specifically, the bound and confound curve takes into account off-shell effects, meaning the neutron inside a nucleus is not in a free state and it does not satisfy the usual energy-momentum relation for a free particle. 

We observe large deviations in the cross-section at very high recoil nucleon momenta, especially when the neutron isn't treated as 'free'. Since we know that the binding effects do affect the cross-section, we have to account for these deviations with other methods.

### PWIA, FSI, and CHEX

<p align = "center" href="url"><img src="https://github.com/MarlenAnalytics/deuteron_electrodisintegration/blob/main/RNPCS.png" height="400" width="550" ></p>

We observe the ratio of the neutron cross-section and the proton cross-section at a fixed value of Q<sup>2</sup> = 4.0 GeV with respect to the recoil nucleon polar angle where each curve represents the different re-scattering events we consider. We see again large deviations at a high recoil nucleon momenta, especially when there is a charge exchange re-scattering. This can mean that protons are being detected instead of neutrons, which is undesirable if we want to extract precise measurements of neutron form-factors.

### Q<sup>2</sup> up to 18.0 GeV

With advancements towards higher energies at Jefferson Lab as well as the Electrion Ion Collider in the future, it was proposed that high precision measurements of the magnetic neutron form-factor can be conducted with Q<sup>2</sup> values between 3.5 GeV and up to 18 GeV.

However, in order to remove any systematic uncertainties and to account for the deviations previously mentioned, we have to calculcate a correction factor. This can be done by using the Ratio Method. In the following visualization we see the Ratio Correction Factor plotted with respect to the polar angle of the struck nucleon. This ratio was calculated by taking the ratio of the stationary cross-section and deuteron cross-section.

<p align = "center" href="url"><img src="https://github.com/MarlenAnalytics/deuteron_electrodisintegration/blob/main/rcf_smooth_updt.png" height="400" width="550" ></p>

We can infer that the charge exchange contribution deviates the most from 1.0, especially as we reach Q<sup>2</sup> = 18.0 GeV. The goal is to provide this data and information to JLAB, so they can then integrate all of it and apply it to experimental measurements.

<p align = "center" href="url"><img src="https://github.com/MarlenAnalytics/deuteron_electrodisintegration/blob/main/Q2_x1.png" height="400" width="550" ></p>

The above figure depicts the logarithmically scaled cross-section plotted with respect to polar angle of the struck nucleon with respect to q, at varying values of Q<sup>2</sup>. We set Bjorken x equal to 1, which means that the momentum transfer in the scattering process is equal to the momentum of the struck nucleon. The virtual photon (q) interacts with a nucleon in such a way that the nucleon receives all the momentum transferred from the photon without any additional energy loss or gain. We again see that the FSI and CHEX contributions deviate heavily, from the 'stationary free nucleon' cross-section, reinforcing that the binding effects play a significant role and need to be accounted for.

## Results

We infer from our analysis, that in scenarios involving high momentum within the framework of PWIA, FSI, andd CHEX, the detection can yield to protons rather than neutrons. To rectify this, a correction factor is essential to accomodate fluctuations in the nucleon cross-section and accurately identify the detected particle as a neutron if we want high precision measurements of the neutron form-factors.

  ## References
  
  S. Riordan et al., Phys. Rev. Lett. 105, 262302 (2010).

  S. Rock, R. G. Arnold, P. E. Bosted, B. T. Chertok, B. A. Mecking, I. A. Schmidt, Z. M.
Szalata, R. York, and R. Zdarko, Phys. Rev. Lett. 49, 1139 (1982). 10

  S. Rock, R. G. Arnold, P. E. Bosted, B. T. Chertok, B. A. Mecking, I. A. Schmidt, Z. M. Szalata, R. York, and R. Zdarko, Phys. Rev. D 46, 24 (1992).

  L. L. Frankfurt, M. M. Sargsian, and M. I. Strikman, Phys. Rev. C 56, 1124 (1997).

  J.-M. Laget, in Workshop on Color Transparency (CT 97) (1998) pp. 121–129.

  M. M. Sargsian, Phys. Rev. C 82, 014612 (2010).

  M. M. Sargsian, Int. J. Mod. Phys. E 10, 405 (2001).


  ## Acknowledgements

  This work is in partnership with Florida International University and Thomas Jefferson National Accelerator Facility and is supported by the U.S. DOE Office of Science grant for Undergraduate Internships DE-SC0022007 and Office of Nuclear Physics grant DE-FG02-01ER41172.

  ## Questions

  For any further questions you may contact me or my mentors at the following:

  Misak Sargsian: sargsian@fiu.edu
  
  Wim Cosyn: wcosyn@fiu.edu
  
  Lei Guo: leguo@fiu.edu
