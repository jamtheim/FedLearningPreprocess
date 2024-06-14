<?xml version="1.0" encoding="utf-8"?>
<MICE Version="2022.4.9.0" Timestamp="2024-06-14 13:48:11.7626550">
  <Settings>
    <ID>73068622-02ab-4606-b89e-871354cd6c39</ID>
    <Name>New Process</Name>
    <Description />
    <Version>1.0</Version>
    <Compress>False</Compress>
  </Settings>
  <Nodes>
    <Node ID="84e1fbcBFf0FA25D" T="NodeIORepeater" V="0.1" X="392" Y="433" FI="">
      <Inputs>
        <IO ID="F4bAc5CCe1c6a5c6" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="BB8Adaaf7Bf01DfB" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="CT" />
        <SN N="Sim" V="True" />
        <SN N="SetNewName" V="True" />
        <SN N="IOType" V="Mice.Types.Image4DFloat" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="6D718B5f5DFae81f" T="NodeIORepeater" V="0.1" X="392" Y="487" FI="">
      <Inputs>
        <IO ID="3DaCC31E44C4F433" T="RegistrationCollection" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="B31A4C2cce25C6eE" T="RegistrationCollection" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="REG" />
        <SN N="Sim" V="True" />
        <SN N="SetNewName" V="False" />
        <SN N="IOType" V="Mice.Types.RegistrationCollection" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="faD7708ADdF5fDB6" T="NodeIORepeater" V="0.1" X="890" Y="246" FI="">
      <Inputs>
        <IO ID="c247fb015De1AaCA" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="7cDFBEf6F63A8c5C" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="CTV" />
        <SN N="Sim" V="False" />
        <SN N="SetNewName" V="True" />
        <SN N="IOType" V="Mice.Types.Image4DFloat" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="3A0bd472aca0d48c" T="NodeIORepeater" V="0.1" X="392" Y="460" FI="">
      <Inputs>
        <IO ID="F4cf7fDfC234aaAf" T="RTStructCollection" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="7c8deBdbCd6D1FA1" T="RTStructCollection" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="Structures" />
        <SN N="Sim" V="True" />
        <SN N="SetNewName" V="False" />
        <SN N="IOType" V="Mice.Types.RTStructCollection" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="a2EADFF6Ccaf1BD2" T="NodeReadDicomDB" V="0.1" X="234" Y="421" FI="">
      <Inputs />
      <Outputs>
        <IO ID="1C564CC6af6bD0cd" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="34CEa1d1C7dcFc0e" T="RTStructCollection" N="Structures" MI="1" MA="1" />
        <IO ID="e2cED74F35a6Bad8" T="RegistrationCollection" N="Registrations" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="SeriesID" V="159" />
        <SN N="IStructs" V="True" />
        <SN N="StructSeriesIDs" V="164" />
        <SN N="IRegs" V="True" />
        <SN N="RegSeriesIDs" V="161" />
        <SN N="Connection" V="MRIOnlyBrainDoseExtractV1" />
        <SN N="DateOffset" V="0" />
        <SN N="MatchString" V="RT p+ Skalle  2.0  H30s" />
        <SN N="IgnoreBatch" V="False" />
        <SN N="TagsSet" V="All" />
        <SN N="PrivateTags" V="False" />
        <SN N="SetNewName" V="False" />
        <SN N="NewName" V="" />
        <SN N="UseStructFilter" V="False" />
        <SN N="StructName" V="" />
        <SN N="Cond" V="Contains" />
        <SN N="CaseSensitive" V="False" />
        <SN N="Action" V="Keep" />
        <SN N="MiceType" V="Image4DFloat" />
        <SN N="DataSeriesIDs" V="" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="EEF5FbE0fABFd7d3" T="NodeReadDicomDB" V="0.1" X="234" Y="530" FI="">
      <Inputs />
      <Outputs>
        <IO ID="bd55D3e14C1b1abc" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="bC4C2F2cf63b6cfD" T="RTStructCollection" N="Structures" MI="1" MA="1" />
        <IO ID="1C8ADF72B51fC25A" T="RegistrationCollection" N="Registrations" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="SeriesID" V="162" />
        <SN N="IStructs" V="True" />
        <SN N="StructSeriesIDs" V="164" />
        <SN N="IRegs" V="True" />
        <SN N="RegSeriesIDs" V="161" />
        <SN N="Connection" V="MRIOnlyBrainDoseExtractV1" />
        <SN N="DateOffset" V="0" />
        <SN N="MatchString" V="Eclipse Doses" />
        <SN N="IgnoreBatch" V="False" />
        <SN N="TagsSet" V="All" />
        <SN N="PrivateTags" V="False" />
        <SN N="SetNewName" V="False" />
        <SN N="NewName" V="" />
        <SN N="UseStructFilter" V="False" />
        <SN N="StructName" V="" />
        <SN N="Cond" V="Contains" />
        <SN N="CaseSensitive" V="False" />
        <SN N="Action" V="Keep" />
        <SN N="MiceType" V="Image4DFloat" />
        <SN N="DataSeriesIDs" V="" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="7DD8C2b11be6155A" T="NodeExportNIfTI" V="0.1" X="1314" Y="1256" FI="">
      <Inputs>
        <IO ID="B56AB0b80AdCf2aa" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs />
      <Settings>
        <SN N="ImagePrefix" V="" />
        <SN N="Compress" V="True" />
        <SN N="Metadata" V="False" />
        <SN N="OutPath" V="C:\Mice Export" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="aAf0b6ADF7aF3B14" T="NodeIORepeater" V="0.1" X="890" Y="1256" FI="">
      <Inputs>
        <IO ID="7C8f2dc18CDf56c0" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="0B14FACB0a4dd7cF" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="dose" />
        <SN N="Sim" V="False" />
        <SN N="SetNewName" V="True" />
        <SN N="IOType" V="Mice.Types.Image4DFloat" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="168FDCC3E148b623" T="NodeResampleImageFilter" V="0.1" X="700" Y="1249" FI="">
      <Inputs>
        <IO ID="68121620EeCfAcAE" T="Image4DFloat" N="Reference" MI="1" MA="1" />
        <IO ID="63D42D2618e5Ed47" T="Image4DFloat" N="Input" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="36fB5beB62Fc8a3F" T="Image4DFloat" N="Output" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Interpolator" V="Linear" />
        <SN N="SetNewFOR" V="True" />
        <SN N="DVal" V="0" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="Af1adDE7DAFefFf4" T="NodeIORepeater" V="0.1" X="392" Y="575" FI="">
      <Inputs>
        <IO ID="0e2EEf2C13f60AE3" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="6CD8B62DEf6b7F38" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="doseImage" />
        <SN N="Sim" V="True" />
        <SN N="SetNewName" V="True" />
        <SN N="IOType" V="Mice.Types.Image4DFloat" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="aaffa4561a3ad3f7" T="NodeExportNIfTI" V="0.1" X="1316" Y="246" FI="">
      <Inputs>
        <IO ID="acdD2aAc0e62dadA" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs />
      <Settings>
        <SN N="ImagePrefix" V="" />
        <SN N="Compress" V="True" />
        <SN N="Metadata" V="False" />
        <SN N="OutPath" V="C:\Mice Export" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="c0dF8f6Ecfd0Ed02" T="NodeStructProcessor" V="0.1" X="688" Y="232" FI="Structure Name(s);">
      <Inputs>
        <IO ID="8D2C1efA5eAD3A6a" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="7e2Ae5B2a84FdCc8" T="RTStructCollection" N="Structures" MI="1" MA="1" />
        <IO ID="aBacf4f68CcB88b0" T="String" N="Structure Name(s)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="Edb3fAcDA60bB382" T="Image4DBool" N="Mask" MI="1" MA="1" />
        <IO ID="3ceD1eA6D5050A7B" T="Image4DFloat" N="Smooth Mask" MI="1" MA="1" />
        <IO ID="BaEdBabe1ba73E0B" T="DataCollection" N="Statistics" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="StructName" V="" />
        <SN N="Cond" V="Regex" />
        <SN N="CaseSensitive" V="False" />
        <SN N="DSS" V="False" />
        <SN N="MError" V="0.08" />
        <SN N="MIter" V="5" />
        <SN N="UseSc" V="False" />
        <SN N="SCond" V="15" />
        <SN N="ISampleMethod" V="None" />
        <SN N="DivX" V="1" />
        <SN N="DivY" V="1" />
        <SN N="DivZ" V="1" />
        <SN N="NumPoints" V="1000" />
        <SN N="AISampleMethod" V="None" />
        <SN N="ADivX" V="1" />
        <SN N="ADivY" V="1" />
        <SN N="ADivZ" V="1" />
        <SN N="ANumPoints" V="1000" />
        <SN N="Threshold" V="50" />
        <SN N="DivType" V="HigherOrEqual" />
        <SN N="Ect" V="0.0001" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="C2E2c10Ee416C57C" T="NodeResampleImageResolution" V="0.1" X="1042" Y="1236" FI="New Voxel Size X (mm);New Voxel Size Y (mm);New Voxel Size Z (mm);">
      <Inputs>
        <IO ID="4CCccEA1e8A4C0ac" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="Af6CBf6e4C68182A" T="Double" N="New Voxel Size X (mm)" MI="1" MA="1" />
        <IO ID="d83D13DDEaDAa35A" T="Double" N="New Voxel Size Y (mm)" MI="1" MA="1" />
        <IO ID="b881B540c33E4aC4" T="Double" N="New Voxel Size Z (mm)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="16ab665A27cCaF22" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="VoxelSizeX" V="3" />
        <SN N="VoxelSizeY" V="3" />
        <SN N="VoxelSizeZ" V="3" />
        <SN N="Interpolator" V="Linear" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="cBCCD5a131EcCBfB" T="NodeGenerateDouble" V="0.1" X="234" Y="229" FI="">
      <Inputs />
      <Outputs>
        <IO ID="0F718b8AdcB7a72D" T="Double" N="Value" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="V" V="3" />
        <SN N="VariableName" V="X" />
        <SN N="SC" V="True" />
        <SN N="IsBatchVariable" V="False" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="cAF024788A77E3aF" T="NodeResampleImageResolution" V="0.1" X="1044" Y="226" FI="New Voxel Size X (mm);New Voxel Size Y (mm);New Voxel Size Z (mm);">
      <Inputs>
        <IO ID="B1f418feD8ba1acf" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="1D3dc28ebaBBcc0a" T="Double" N="New Voxel Size X (mm)" MI="1" MA="1" />
        <IO ID="B605b5c8CAB1B087" T="Double" N="New Voxel Size Y (mm)" MI="1" MA="1" />
        <IO ID="eFD0BBA12a2007cA" T="Double" N="New Voxel Size Z (mm)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="Cb14CAd5A435BA6E" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="VoxelSizeX" V="3" />
        <SN N="VoxelSizeY" V="3" />
        <SN N="VoxelSizeZ" V="3" />
        <SN N="Interpolator" V="NearestNeighbour" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="7d0bC78FBEeA2F6B" T="NodeIORepeater" V="0.1" X="392" Y="225" FI="">
      <Inputs>
        <IO ID="1478ad20B57fab4f" T="Double" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="8FdB58AE02A0C23f" T="Double" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="res X" />
        <SN N="Sim" V="True" />
        <SN N="SetNewName" V="False" />
        <SN N="IOType" V="System.Double" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="c8Ab5d1Aa3EeC4B1" T="NodeIORepeater" V="0.1" X="392" Y="279" FI="">
      <Inputs>
        <IO ID="6EeE11fd5b63fCBD" T="Double" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="6Ae8A6Fa42AbAE3C" T="Double" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="res Z" />
        <SN N="Sim" V="True" />
        <SN N="SetNewName" V="False" />
        <SN N="IOType" V="System.Double" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="7c3B1e12eEa724C2" T="NodeIORepeater" V="0.1" X="392" Y="252" FI="">
      <Inputs>
        <IO ID="27F80cF3cDD37bce" T="Double" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="845af5C041AbAFf0" T="Double" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="res Y" />
        <SN N="Sim" V="True" />
        <SN N="SetNewName" V="False" />
        <SN N="IOType" V="System.Double" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="1DE2f2f07cd16F3A" T="NodeGenerateDouble" V="0.1" X="234" Y="256" FI="">
      <Inputs />
      <Outputs>
        <IO ID="d6b054Fbb1c547c7" T="Double" N="Value" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="V" V="3" />
        <SN N="VariableName" V="Y" />
        <SN N="SC" V="True" />
        <SN N="IsBatchVariable" V="False" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="8543da3FcD6554Bf" T="NodeGenerateDouble" V="0.1" X="234" Y="283" FI="">
      <Inputs />
      <Outputs>
        <IO ID="5f33aEF646CB85CB" T="Double" N="Value" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="V" V="3" />
        <SN N="VariableName" V="Z" />
        <SN N="SC" V="True" />
        <SN N="IsBatchVariable" V="False" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="e27a6DCCda3cc1bf" T="NodeIORepeater" V="0.1" X="890" Y="347" FI="">
      <Inputs>
        <IO ID="c0Cf3bA70c2B21bf" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="B75D8DfaBEe8742A" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="PTV" />
        <SN N="Sim" V="False" />
        <SN N="SetNewName" V="True" />
        <SN N="IOType" V="Mice.Types.Image4DFloat" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="5ABBE4dEBAec0F3a" T="NodeStructProcessor" V="0.1" X="687" Y="333" FI="Structure Name(s);">
      <Inputs>
        <IO ID="Cb8C401EFFc1b6fA" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="FEae5648ECC0bf7d" T="RTStructCollection" N="Structures" MI="1" MA="1" />
        <IO ID="fd6EeBB48cD832cB" T="String" N="Structure Name(s)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="b2DA7eedCf62CEa3" T="Image4DBool" N="Mask" MI="1" MA="1" />
        <IO ID="BEbdd23EA86BebCf" T="Image4DFloat" N="Smooth Mask" MI="1" MA="1" />
        <IO ID="07FCC8CBf640ab08" T="DataCollection" N="Statistics" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="StructName" V="" />
        <SN N="Cond" V="Regex" />
        <SN N="CaseSensitive" V="False" />
        <SN N="DSS" V="False" />
        <SN N="MError" V="0.08" />
        <SN N="MIter" V="5" />
        <SN N="UseSc" V="False" />
        <SN N="SCond" V="15" />
        <SN N="ISampleMethod" V="None" />
        <SN N="DivX" V="1" />
        <SN N="DivY" V="1" />
        <SN N="DivZ" V="1" />
        <SN N="NumPoints" V="1000" />
        <SN N="AISampleMethod" V="None" />
        <SN N="ADivX" V="1" />
        <SN N="ADivY" V="1" />
        <SN N="ADivZ" V="1" />
        <SN N="ANumPoints" V="1000" />
        <SN N="Threshold" V="50" />
        <SN N="DivType" V="HigherOrEqual" />
        <SN N="Ect" V="0.0001" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="755CEEE1Dc8b37fd" T="NodeResampleImageResolution" V="0.1" X="1043" Y="327" FI="New Voxel Size X (mm);New Voxel Size Y (mm);New Voxel Size Z (mm);">
      <Inputs>
        <IO ID="7D4Cada4C4DD52E5" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="D4FC5DD8FeF5d5D1" T="Double" N="New Voxel Size X (mm)" MI="1" MA="1" />
        <IO ID="2DCDBcde7eccC0ae" T="Double" N="New Voxel Size Y (mm)" MI="1" MA="1" />
        <IO ID="11ad710Da5551e1F" T="Double" N="New Voxel Size Z (mm)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="A53BAbDA0AD1ABF8" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="VoxelSizeX" V="3" />
        <SN N="VoxelSizeY" V="3" />
        <SN N="VoxelSizeZ" V="3" />
        <SN N="Interpolator" V="NearestNeighbour" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="8D1Cf651d7D28AeA" T="NodeExportNIfTI" V="0.1" X="1315" Y="347" FI="">
      <Inputs>
        <IO ID="cF3f54c1d16bCB3a" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs />
      <Settings>
        <SN N="ImagePrefix" V="" />
        <SN N="Compress" V="True" />
        <SN N="Metadata" V="False" />
        <SN N="OutPath" V="C:\Mice Export" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="7b7c8522EfDC5CC7" T="NodeIORepeater" V="0.1" X="890" Y="448" FI="">
      <Inputs>
        <IO ID="cdF52EEBdd2bCFAd" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="0dcFCBBA4bDEfCDC" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="brainstem" />
        <SN N="Sim" V="False" />
        <SN N="SetNewName" V="True" />
        <SN N="IOType" V="Mice.Types.Image4DFloat" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="dd3Bb8f4D7c4fcCC" T="NodeStructProcessor" V="0.1" X="687" Y="434" FI="Structure Name(s);">
      <Inputs>
        <IO ID="BbDC01bfd32B68a2" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="165C8DDa0Af845b0" T="RTStructCollection" N="Structures" MI="1" MA="1" />
        <IO ID="bEAE75275fFaef1c" T="String" N="Structure Name(s)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="B3abFAc44c4c31A8" T="Image4DBool" N="Mask" MI="1" MA="1" />
        <IO ID="cEDDF0761C5fCbEA" T="Image4DFloat" N="Smooth Mask" MI="1" MA="1" />
        <IO ID="1b8c88dB4a051Af7" T="DataCollection" N="Statistics" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="StructName" V="" />
        <SN N="Cond" V="Regex" />
        <SN N="CaseSensitive" V="False" />
        <SN N="DSS" V="False" />
        <SN N="MError" V="0.08" />
        <SN N="MIter" V="5" />
        <SN N="UseSc" V="False" />
        <SN N="SCond" V="15" />
        <SN N="ISampleMethod" V="None" />
        <SN N="DivX" V="1" />
        <SN N="DivY" V="1" />
        <SN N="DivZ" V="1" />
        <SN N="NumPoints" V="1000" />
        <SN N="AISampleMethod" V="None" />
        <SN N="ADivX" V="1" />
        <SN N="ADivY" V="1" />
        <SN N="ADivZ" V="1" />
        <SN N="ANumPoints" V="1000" />
        <SN N="Threshold" V="50" />
        <SN N="DivType" V="HigherOrEqual" />
        <SN N="Ect" V="0.0001" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="F72D3FeE2eC73ccD" T="NodeResampleImageResolution" V="0.1" X="1043" Y="428" FI="New Voxel Size X (mm);New Voxel Size Y (mm);New Voxel Size Z (mm);">
      <Inputs>
        <IO ID="06ed6Ff5A27A8032" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="5c800AFD0D3C5c1f" T="Double" N="New Voxel Size X (mm)" MI="1" MA="1" />
        <IO ID="f26c6cD01C5Ef0bC" T="Double" N="New Voxel Size Y (mm)" MI="1" MA="1" />
        <IO ID="E1bBcfBAB40D55ae" T="Double" N="New Voxel Size Z (mm)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="a2bf20432B7eEad8" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="VoxelSizeX" V="3" />
        <SN N="VoxelSizeY" V="3" />
        <SN N="VoxelSizeZ" V="3" />
        <SN N="Interpolator" V="NearestNeighbour" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="FaFdebf22CA7cF00" T="NodeExportNIfTI" V="0.1" X="1315" Y="448" FI="">
      <Inputs>
        <IO ID="BCa256267ae2080e" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs />
      <Settings>
        <SN N="ImagePrefix" V="" />
        <SN N="Compress" V="True" />
        <SN N="Metadata" V="False" />
        <SN N="OutPath" V="C:\Mice Export" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="A72eaBe458B6Fc8E" T="NodeStructProcessor" V="0.1" X="687" Y="535" FI="Structure Name(s);">
      <Inputs>
        <IO ID="eae03128E334Ebf0" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="27cbcC4fdFe561F6" T="RTStructCollection" N="Structures" MI="1" MA="1" />
        <IO ID="CCd7d4E7607F6408" T="String" N="Structure Name(s)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="7a24f1fc274c338D" T="Image4DBool" N="Mask" MI="1" MA="1" />
        <IO ID="e4D5ebE5e7DeD5b5" T="Image4DFloat" N="Smooth Mask" MI="1" MA="1" />
        <IO ID="d56DCEAa2aCe12FC" T="DataCollection" N="Statistics" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="StructName" V="" />
        <SN N="Cond" V="Regex" />
        <SN N="CaseSensitive" V="False" />
        <SN N="DSS" V="False" />
        <SN N="MError" V="0.08" />
        <SN N="MIter" V="5" />
        <SN N="UseSc" V="False" />
        <SN N="SCond" V="15" />
        <SN N="ISampleMethod" V="None" />
        <SN N="DivX" V="1" />
        <SN N="DivY" V="1" />
        <SN N="DivZ" V="1" />
        <SN N="NumPoints" V="1000" />
        <SN N="AISampleMethod" V="None" />
        <SN N="ADivX" V="1" />
        <SN N="ADivY" V="1" />
        <SN N="ADivZ" V="1" />
        <SN N="ANumPoints" V="1000" />
        <SN N="Threshold" V="50" />
        <SN N="DivType" V="HigherOrEqual" />
        <SN N="Ect" V="0.0001" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="3c1eFeAdec4c6dF0" T="NodeIORepeater" V="0.1" X="890" Y="549" FI="">
      <Inputs>
        <IO ID="AFA231Fa27241Edf" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="2a8dD807AE351F4E" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="optic_chiasm" />
        <SN N="Sim" V="False" />
        <SN N="SetNewName" V="True" />
        <SN N="IOType" V="Mice.Types.Image4DFloat" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="e80aC17EF6B4cDf3" T="NodeResampleImageResolution" V="0.1" X="1043" Y="529" FI="New Voxel Size X (mm);New Voxel Size Y (mm);New Voxel Size Z (mm);">
      <Inputs>
        <IO ID="2b8a26E5eFdFb055" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="d5eb11b6B123bBB2" T="Double" N="New Voxel Size X (mm)" MI="1" MA="1" />
        <IO ID="38E53BEf2B8b53c1" T="Double" N="New Voxel Size Y (mm)" MI="1" MA="1" />
        <IO ID="D52eb05bab2ae346" T="Double" N="New Voxel Size Z (mm)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="eE5cb8c5A8Cf18a0" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="VoxelSizeX" V="3" />
        <SN N="VoxelSizeY" V="3" />
        <SN N="VoxelSizeZ" V="3" />
        <SN N="Interpolator" V="NearestNeighbour" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="b2127d0fe8dbeb5d" T="NodeExportNIfTI" V="0.1" X="1315" Y="549" FI="">
      <Inputs>
        <IO ID="7D02CE7cc471bc08" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs />
      <Settings>
        <SN N="ImagePrefix" V="" />
        <SN N="Compress" V="True" />
        <SN N="Metadata" V="False" />
        <SN N="OutPath" V="C:\Mice Export" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="6fd5ef5c444352F5" T="NodeGenerateString" V="0.1" X="484" Y="296" FI="">
      <Inputs />
      <Outputs>
        <IO ID="e35d50B3Fccb6f16" T="String" N="Value" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="V" V="^CTV.*" />
        <SN N="VariableName" V="CTV" />
        <SN N="SC" V="True" />
        <SN N="IsBatchVariable" V="False" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="bC76ee1F2C20D8D7" T="NodeGenerateString" V="0.1" X="484" Y="397" FI="">
      <Inputs />
      <Outputs>
        <IO ID="80f3aCF0Dff3DAAF" T="String" N="Value" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="V" V="^PTV.*" />
        <SN N="VariableName" V="PTV" />
        <SN N="SC" V="True" />
        <SN N="IsBatchVariable" V="False" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="fC8CCCEa6bFf63FD" T="NodeGenerateString" V="0.1" X="484" Y="498" FI="">
      <Inputs />
      <Outputs>
        <IO ID="a5E150AB38Fdc6F2" T="String" N="Value" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="V" V="^BrainStem" />
        <SN N="VariableName" V="Brainstem" />
        <SN N="SC" V="True" />
        <SN N="IsBatchVariable" V="False" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="E4dfDdf8DbbcfC6b" T="NodeGenerateString" V="0.1" X="484" Y="599" FI="">
      <Inputs />
      <Outputs>
        <IO ID="ffB62B3B2feDB30E" T="String" N="Value" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="V" V="^Chiasm" />
        <SN N="VariableName" V="Chiasm" />
        <SN N="SC" V="True" />
        <SN N="IsBatchVariable" V="False" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="1aDBa1d35AcDbf02" T="NodeExportNIfTI" V="0.1" X="1314" Y="1155" FI="">
      <Inputs>
        <IO ID="31Cf2fE50d07c54A" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs />
      <Settings>
        <SN N="ImagePrefix" V="" />
        <SN N="Compress" V="True" />
        <SN N="Metadata" V="False" />
        <SN N="OutPath" V="C:\Mice Export" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="FC6De46BD058baa6" T="NodeResampleImageResolution" V="0.1" X="1042" Y="1135" FI="New Voxel Size X (mm);New Voxel Size Y (mm);New Voxel Size Z (mm);">
      <Inputs>
        <IO ID="aDa63aAB1bdAf03A" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="E7Ca4484ec8114BF" T="Double" N="New Voxel Size X (mm)" MI="1" MA="1" />
        <IO ID="e3fA45F1ac6065af" T="Double" N="New Voxel Size Y (mm)" MI="1" MA="1" />
        <IO ID="60afBb8eDe10b236" T="Double" N="New Voxel Size Z (mm)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="20cFACF1C4a17C7C" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="VoxelSizeX" V="3" />
        <SN N="VoxelSizeY" V="3" />
        <SN N="VoxelSizeZ" V="3" />
        <SN N="Interpolator" V="Linear" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="867bd084Fa10EDDB" T="NodeGenerateString" V="0.1" X="484" Y="700" FI="">
      <Inputs />
      <Outputs>
        <IO ID="bF0dAaEcEAb3BA8d" T="String" N="Value" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="V" V="^Eye_L" />
        <SN N="VariableName" V="globe_L" />
        <SN N="SC" V="True" />
        <SN N="IsBatchVariable" V="False" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="BfCD28eAe42FC1f6" T="NodeStructProcessor" V="0.1" X="687" Y="636" FI="Structure Name(s);">
      <Inputs>
        <IO ID="badEDfE7F2b407FF" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="3F76661cde8DAc6f" T="RTStructCollection" N="Structures" MI="1" MA="1" />
        <IO ID="A5bec6D22CDbfE61" T="String" N="Structure Name(s)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="5cBC2C7dBaBeAa1D" T="Image4DBool" N="Mask" MI="1" MA="1" />
        <IO ID="44E36BC5bfdEC062" T="Image4DFloat" N="Smooth Mask" MI="1" MA="1" />
        <IO ID="BA1e4D06775bFfC1" T="DataCollection" N="Statistics" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="StructName" V="" />
        <SN N="Cond" V="Regex" />
        <SN N="CaseSensitive" V="False" />
        <SN N="DSS" V="False" />
        <SN N="MError" V="0.08" />
        <SN N="MIter" V="5" />
        <SN N="UseSc" V="False" />
        <SN N="SCond" V="15" />
        <SN N="ISampleMethod" V="None" />
        <SN N="DivX" V="1" />
        <SN N="DivY" V="1" />
        <SN N="DivZ" V="1" />
        <SN N="NumPoints" V="1000" />
        <SN N="AISampleMethod" V="None" />
        <SN N="ADivX" V="1" />
        <SN N="ADivY" V="1" />
        <SN N="ADivZ" V="1" />
        <SN N="ANumPoints" V="1000" />
        <SN N="Threshold" V="50" />
        <SN N="DivType" V="HigherOrEqual" />
        <SN N="Ect" V="0.0001" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="c2CFb8e667Aa4deb" T="NodeIORepeater" V="0.1" X="890" Y="650" FI="">
      <Inputs>
        <IO ID="eb75CCfAB8fCf5aB" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="eE033BF3a0DA7Cea" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="globe_L" />
        <SN N="Sim" V="False" />
        <SN N="SetNewName" V="True" />
        <SN N="IOType" V="Mice.Types.Image4DFloat" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="0f017AcF2c27A170" T="NodeResampleImageResolution" V="0.1" X="1043" Y="630" FI="New Voxel Size X (mm);New Voxel Size Y (mm);New Voxel Size Z (mm);">
      <Inputs>
        <IO ID="04d4B0D8067e20DA" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="8bE84bFEeAEDDDFf" T="Double" N="New Voxel Size X (mm)" MI="1" MA="1" />
        <IO ID="1aee400e3EAf23bE" T="Double" N="New Voxel Size Y (mm)" MI="1" MA="1" />
        <IO ID="2dAf308Fe20bbaFd" T="Double" N="New Voxel Size Z (mm)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="B1F1CfFCDAfA3A5D" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="VoxelSizeX" V="3" />
        <SN N="VoxelSizeY" V="3" />
        <SN N="VoxelSizeZ" V="3" />
        <SN N="Interpolator" V="NearestNeighbour" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="a82f4Ca8f24f8bAa" T="NodeExportNIfTI" V="0.1" X="1315" Y="650" FI="">
      <Inputs>
        <IO ID="5B312A5EA2c4eabc" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs />
      <Settings>
        <SN N="ImagePrefix" V="" />
        <SN N="Compress" V="True" />
        <SN N="Metadata" V="False" />
        <SN N="OutPath" V="C:\Mice Export" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="c3471186AC1cf475" T="NodeResampleImageResolution" V="0.1" X="1043" Y="731" FI="New Voxel Size X (mm);New Voxel Size Y (mm);New Voxel Size Z (mm);">
      <Inputs>
        <IO ID="88E2eE846FdaaAce" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="c602bEEE0DA6c1E8" T="Double" N="New Voxel Size X (mm)" MI="1" MA="1" />
        <IO ID="DF82ffbEdAfc68Ad" T="Double" N="New Voxel Size Y (mm)" MI="1" MA="1" />
        <IO ID="81B5cEaEEac4db1f" T="Double" N="New Voxel Size Z (mm)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="ae0DBC754cF3eB10" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="VoxelSizeX" V="3" />
        <SN N="VoxelSizeY" V="3" />
        <SN N="VoxelSizeZ" V="3" />
        <SN N="Interpolator" V="NearestNeighbour" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="34FBcC8BFdc86c5f" T="NodeExportNIfTI" V="0.1" X="1315" Y="751" FI="">
      <Inputs>
        <IO ID="B5A5A03ff60EdDEC" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs />
      <Settings>
        <SN N="ImagePrefix" V="" />
        <SN N="Compress" V="True" />
        <SN N="Metadata" V="False" />
        <SN N="OutPath" V="C:\Mice Export" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="1c0ab24280ea1eAf" T="NodeStructProcessor" V="0.1" X="687" Y="737" FI="Structure Name(s);">
      <Inputs>
        <IO ID="2Ca7cc2Cd3b3aFD1" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="B116AFBecc8076f7" T="RTStructCollection" N="Structures" MI="1" MA="1" />
        <IO ID="27b6672faf8e8b0C" T="String" N="Structure Name(s)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="b23Ac1eda448dcDf" T="Image4DBool" N="Mask" MI="1" MA="1" />
        <IO ID="DcabD04D8B6bFdeb" T="Image4DFloat" N="Smooth Mask" MI="1" MA="1" />
        <IO ID="EFEfc85a375bc2c7" T="DataCollection" N="Statistics" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="StructName" V="" />
        <SN N="Cond" V="Regex" />
        <SN N="CaseSensitive" V="False" />
        <SN N="DSS" V="False" />
        <SN N="MError" V="0.08" />
        <SN N="MIter" V="5" />
        <SN N="UseSc" V="False" />
        <SN N="SCond" V="15" />
        <SN N="ISampleMethod" V="None" />
        <SN N="DivX" V="1" />
        <SN N="DivY" V="1" />
        <SN N="DivZ" V="1" />
        <SN N="NumPoints" V="1000" />
        <SN N="AISampleMethod" V="None" />
        <SN N="ADivX" V="1" />
        <SN N="ADivY" V="1" />
        <SN N="ADivZ" V="1" />
        <SN N="ANumPoints" V="1000" />
        <SN N="Threshold" V="50" />
        <SN N="DivType" V="HigherOrEqual" />
        <SN N="Ect" V="0.0001" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="2B6d1688bd316FDE" T="NodeIORepeater" V="0.1" X="890" Y="751" FI="">
      <Inputs>
        <IO ID="B8ECfEA1Fe0beD3e" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="8bF583De2Eb04A6e" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="globe_R" />
        <SN N="Sim" V="False" />
        <SN N="SetNewName" V="True" />
        <SN N="IOType" V="Mice.Types.Image4DFloat" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="EbaC6ae3a083bC0a" T="NodeGenerateString" V="0.1" X="484" Y="801" FI="">
      <Inputs />
      <Outputs>
        <IO ID="BBACfaaaa4eCCfD3" T="String" N="Value" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="V" V="^Eye_R" />
        <SN N="VariableName" V="globe_R" />
        <SN N="SC" V="True" />
        <SN N="IsBatchVariable" V="False" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="71aDA7650b66ccBf" T="NodeExportNIfTI" V="0.1" X="1315" Y="852" FI="">
      <Inputs>
        <IO ID="E5f6c43BB28eF4Ce" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs />
      <Settings>
        <SN N="ImagePrefix" V="" />
        <SN N="Compress" V="True" />
        <SN N="Metadata" V="False" />
        <SN N="OutPath" V="C:\Mice Export" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="eef64DcAE0d8dd42" T="NodeExportNIfTI" V="0.1" X="1315" Y="953" FI="">
      <Inputs>
        <IO ID="F86f5fc17fAdCfe3" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs />
      <Settings>
        <SN N="ImagePrefix" V="" />
        <SN N="Compress" V="True" />
        <SN N="Metadata" V="False" />
        <SN N="OutPath" V="C:\Mice Export" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="0f1c1f33f4eA7Df8" T="NodeResampleImageResolution" V="0.1" X="1043" Y="832" FI="New Voxel Size X (mm);New Voxel Size Y (mm);New Voxel Size Z (mm);">
      <Inputs>
        <IO ID="3f7827Bd1F3a0E5c" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="eE705Ebfaa45dBde" T="Double" N="New Voxel Size X (mm)" MI="1" MA="1" />
        <IO ID="Bcef2e8bA0BCeC78" T="Double" N="New Voxel Size Y (mm)" MI="1" MA="1" />
        <IO ID="2DfFf5Efd172cFaf" T="Double" N="New Voxel Size Z (mm)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="BE1EA0C8E6fec1a1" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="VoxelSizeX" V="3" />
        <SN N="VoxelSizeY" V="3" />
        <SN N="VoxelSizeZ" V="3" />
        <SN N="Interpolator" V="NearestNeighbour" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="731cDbC7367B3b85" T="NodeResampleImageResolution" V="0.1" X="1043" Y="933" FI="New Voxel Size X (mm);New Voxel Size Y (mm);New Voxel Size Z (mm);">
      <Inputs>
        <IO ID="7E1b0B61da341Faf" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="6FD841Bf6Ac2FB01" T="Double" N="New Voxel Size X (mm)" MI="1" MA="1" />
        <IO ID="05Da2b7fC7cB0Dba" T="Double" N="New Voxel Size Y (mm)" MI="1" MA="1" />
        <IO ID="b0D872DAdBdAeeb4" T="Double" N="New Voxel Size Z (mm)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="Dcd5ca040e05Ea2D" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="VoxelSizeX" V="3" />
        <SN N="VoxelSizeY" V="3" />
        <SN N="VoxelSizeZ" V="3" />
        <SN N="Interpolator" V="NearestNeighbour" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="Ba32Bd28B1FaAabC" T="NodeIORepeater" V="0.1" X="890" Y="852" FI="">
      <Inputs>
        <IO ID="dBaeced8dF7ee734" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="B32cF712Cab85874" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="optic_nerve_L" />
        <SN N="Sim" V="False" />
        <SN N="SetNewName" V="True" />
        <SN N="IOType" V="Mice.Types.Image4DFloat" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="BC1AFf5aCdcFA6BC" T="NodeIORepeater" V="0.1" X="890" Y="953" FI="">
      <Inputs>
        <IO ID="B0DeBFe86Bbf46fB" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="a4Cae5cFC51febfb" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="optic_nerve_R" />
        <SN N="Sim" V="False" />
        <SN N="SetNewName" V="True" />
        <SN N="IOType" V="Mice.Types.Image4DFloat" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="Ed0BFd16Cb065CA2" T="NodeStructProcessor" V="0.1" X="687" Y="939" FI="Structure Name(s);">
      <Inputs>
        <IO ID="ca84A36Ea7DC8757" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="06112bBb874BB655" T="RTStructCollection" N="Structures" MI="1" MA="1" />
        <IO ID="fE5C468DFcc3f38e" T="String" N="Structure Name(s)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="Bbf1bB8a274B8Fdc" T="Image4DBool" N="Mask" MI="1" MA="1" />
        <IO ID="c0cDcCc36ecF814f" T="Image4DFloat" N="Smooth Mask" MI="1" MA="1" />
        <IO ID="7F8f1d37F436b0Da" T="DataCollection" N="Statistics" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="StructName" V="" />
        <SN N="Cond" V="Regex" />
        <SN N="CaseSensitive" V="False" />
        <SN N="DSS" V="False" />
        <SN N="MError" V="0.08" />
        <SN N="MIter" V="5" />
        <SN N="UseSc" V="False" />
        <SN N="SCond" V="15" />
        <SN N="ISampleMethod" V="None" />
        <SN N="DivX" V="1" />
        <SN N="DivY" V="1" />
        <SN N="DivZ" V="1" />
        <SN N="NumPoints" V="1000" />
        <SN N="AISampleMethod" V="None" />
        <SN N="ADivX" V="1" />
        <SN N="ADivY" V="1" />
        <SN N="ADivZ" V="1" />
        <SN N="ANumPoints" V="1000" />
        <SN N="Threshold" V="50" />
        <SN N="DivType" V="HigherOrEqual" />
        <SN N="Ect" V="0.0001" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="6D22Abfc68eCA2ca" T="NodeStructProcessor" V="0.1" X="687" Y="838" FI="Structure Name(s);">
      <Inputs>
        <IO ID="21A72Fd0130ba7Ff" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="d364eBe2BDEE3312" T="RTStructCollection" N="Structures" MI="1" MA="1" />
        <IO ID="AA57a0Ba28A3Ea12" T="String" N="Structure Name(s)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="5dc0BaDAC00ea266" T="Image4DBool" N="Mask" MI="1" MA="1" />
        <IO ID="c742c1e0C6bfbDdA" T="Image4DFloat" N="Smooth Mask" MI="1" MA="1" />
        <IO ID="44100aBf6EEC8c8a" T="DataCollection" N="Statistics" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="StructName" V="" />
        <SN N="Cond" V="Regex" />
        <SN N="CaseSensitive" V="False" />
        <SN N="DSS" V="False" />
        <SN N="MError" V="0.08" />
        <SN N="MIter" V="5" />
        <SN N="UseSc" V="False" />
        <SN N="SCond" V="15" />
        <SN N="ISampleMethod" V="None" />
        <SN N="DivX" V="1" />
        <SN N="DivY" V="1" />
        <SN N="DivZ" V="1" />
        <SN N="NumPoints" V="1000" />
        <SN N="AISampleMethod" V="None" />
        <SN N="ADivX" V="1" />
        <SN N="ADivY" V="1" />
        <SN N="ADivZ" V="1" />
        <SN N="ANumPoints" V="1000" />
        <SN N="Threshold" V="50" />
        <SN N="DivType" V="HigherOrEqual" />
        <SN N="Ect" V="0.0001" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="0Bd4eF3d1dA2dDda" T="NodeGenerateString" V="0.1" X="484" Y="902" FI="">
      <Inputs />
      <Outputs>
        <IO ID="6bd250b6dD2b66B2" T="String" N="Value" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="V" V="^OpticNerve_L" />
        <SN N="VariableName" V="Optic Nerve L" />
        <SN N="SC" V="True" />
        <SN N="IsBatchVariable" V="False" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="5ac0ACAb60ccFC65" T="NodeGenerateString" V="0.1" X="484" Y="1003" FI="">
      <Inputs />
      <Outputs>
        <IO ID="dcB057FdcB0AFA3d" T="String" N="Value" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="V" V="^OpticNerve_R" />
        <SN N="VariableName" V="Optic Nerve R" />
        <SN N="SC" V="True" />
        <SN N="IsBatchVariable" V="False" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="BcEc14c66CD1b144" T="NodeExportNIfTI" V="0.1" X="1315" Y="1054" FI="">
      <Inputs>
        <IO ID="0cAaf68Feefc6E54" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs />
      <Settings>
        <SN N="ImagePrefix" V="" />
        <SN N="Compress" V="True" />
        <SN N="Metadata" V="False" />
        <SN N="OutPath" V="C:\Mice Export" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="A1af0ca6AccCdd10" T="NodeResampleImageResolution" V="0.1" X="1043" Y="1034" FI="New Voxel Size X (mm);New Voxel Size Y (mm);New Voxel Size Z (mm);">
      <Inputs>
        <IO ID="1Df70eB1241a8faa" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="1c5B8af4013f3a1F" T="Double" N="New Voxel Size X (mm)" MI="1" MA="1" />
        <IO ID="46Bd4eBA8F2eCbbA" T="Double" N="New Voxel Size Y (mm)" MI="1" MA="1" />
        <IO ID="6F32DdB0dEA8Db61" T="Double" N="New Voxel Size Z (mm)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="dcfb66eC3EBDBbBE" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="VoxelSizeX" V="3" />
        <SN N="VoxelSizeY" V="3" />
        <SN N="VoxelSizeZ" V="3" />
        <SN N="Interpolator" V="NearestNeighbour" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="C82ffa633a1bF1ad" T="NodeIORepeater" V="0.1" X="890" Y="1054" FI="">
      <Inputs>
        <IO ID="1E4A8c20aA588d50" T="Image4DFloat" N="In" MI="1" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="E6ebb5e725fcDfdD" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Desc" V="body" />
        <SN N="Sim" V="False" />
        <SN N="SetNewName" V="True" />
        <SN N="IOType" V="Mice.Types.Image4DFloat" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="8aEfbcCdD5Ad504C" T="NodeStructProcessor" V="0.1" X="687" Y="1040" FI="Structure Name(s);">
      <Inputs>
        <IO ID="aB2FF0d1Da8F8B7E" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="CFDbC3B7dA7CbE4A" T="RTStructCollection" N="Structures" MI="1" MA="1" />
        <IO ID="5DCdfE7fb68e2F8e" T="String" N="Structure Name(s)" MI="1" MA="1" />
      </Inputs>
      <Outputs>
        <IO ID="5Ba83eBA83Cf14F7" T="Image4DBool" N="Mask" MI="1" MA="1" />
        <IO ID="f13F84e70d8F3df0" T="Image4DFloat" N="Smooth Mask" MI="1" MA="1" />
        <IO ID="B3F3D401ccdEb20A" T="DataCollection" N="Statistics" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="StructName" V="" />
        <SN N="Cond" V="Regex" />
        <SN N="CaseSensitive" V="False" />
        <SN N="DSS" V="False" />
        <SN N="MError" V="0.08" />
        <SN N="MIter" V="5" />
        <SN N="UseSc" V="False" />
        <SN N="SCond" V="15" />
        <SN N="ISampleMethod" V="None" />
        <SN N="DivX" V="1" />
        <SN N="DivY" V="1" />
        <SN N="DivZ" V="1" />
        <SN N="NumPoints" V="1000" />
        <SN N="AISampleMethod" V="None" />
        <SN N="ADivX" V="1" />
        <SN N="ADivY" V="1" />
        <SN N="ADivZ" V="1" />
        <SN N="ANumPoints" V="1000" />
        <SN N="Threshold" V="50" />
        <SN N="DivType" V="HigherOrEqual" />
        <SN N="Ect" V="0.0001" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="F64211c167F221dd" T="NodeGenerateString" V="0.1" X="484" Y="1104" FI="">
      <Inputs />
      <Outputs>
        <IO ID="01e2de47EE0BBaCf" T="String" N="Value" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="V" V="^BODY" />
        <SN N="VariableName" V="Body/External" />
        <SN N="SC" V="True" />
        <SN N="IsBatchVariable" V="False" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
    <Node ID="6FaA426A3c2A2718" T="NodeImageDivide" V="0.1" X="1249" Y="1269" FI="">
      <Inputs>
        <IO ID="bA2d8ea5D1F7BA2c" T="Image4DFloat" N="Image" MI="1" MA="1" />
        <IO ID="EFfAbba4ACF86553" T="Image4DFloat" N="Divide Images" MI="0" MA="2147483647" />
      </Inputs>
      <Outputs>
        <IO ID="C7a5bf42Baa658b8" T="Image4DFloat" N="Out" MI="1" MA="1" />
      </Outputs>
      <Settings>
        <SN N="Scalar" V="60" />
        <SN N="RunSingle" V="False" />
      </Settings>
    </Node>
  </Nodes>
  <Connections>
    <CN ID1="F4bAc5CCe1c6a5c6" ID2="1C564CC6af6bD0cd" />
    <CN ID1="3DaCC31E44C4F433" ID2="e2cED74F35a6Bad8" />
    <CN ID1="c247fb015De1AaCA" ID2="3ceD1eA6D5050A7B" />
    <CN ID1="F4cf7fDfC234aaAf" ID2="34CEa1d1C7dcFc0e" />
    <CN ID1="B56AB0b80AdCf2aa" ID2="C7a5bf42Baa658b8" />
    <CN ID1="7C8f2dc18CDf56c0" ID2="36fB5beB62Fc8a3F" />
    <CN ID1="68121620EeCfAcAE" ID2="BB8Adaaf7Bf01DfB" />
    <CN ID1="63D42D2618e5Ed47" ID2="6CD8B62DEf6b7F38" />
    <CN ID1="0e2EEf2C13f60AE3" ID2="bd55D3e14C1b1abc" />
    <CN ID1="acdD2aAc0e62dadA" ID2="Cb14CAd5A435BA6E" />
    <CN ID1="8D2C1efA5eAD3A6a" ID2="BB8Adaaf7Bf01DfB" />
    <CN ID1="7e2Ae5B2a84FdCc8" ID2="7c8deBdbCd6D1FA1" />
    <CN ID1="aBacf4f68CcB88b0" ID2="e35d50B3Fccb6f16" />
    <CN ID1="4CCccEA1e8A4C0ac" ID2="0B14FACB0a4dd7cF" />
    <CN ID1="Af6CBf6e4C68182A" ID2="8FdB58AE02A0C23f" />
    <CN ID1="d83D13DDEaDAa35A" ID2="845af5C041AbAFf0" />
    <CN ID1="b881B540c33E4aC4" ID2="6Ae8A6Fa42AbAE3C" />
    <CN ID1="B1f418feD8ba1acf" ID2="7cDFBEf6F63A8c5C" />
    <CN ID1="1D3dc28ebaBBcc0a" ID2="8FdB58AE02A0C23f" />
    <CN ID1="B605b5c8CAB1B087" ID2="845af5C041AbAFf0" />
    <CN ID1="eFD0BBA12a2007cA" ID2="6Ae8A6Fa42AbAE3C" />
    <CN ID1="1478ad20B57fab4f" ID2="0F718b8AdcB7a72D" />
    <CN ID1="6EeE11fd5b63fCBD" ID2="5f33aEF646CB85CB" />
    <CN ID1="27F80cF3cDD37bce" ID2="d6b054Fbb1c547c7" />
    <CN ID1="c0Cf3bA70c2B21bf" ID2="BEbdd23EA86BebCf" />
    <CN ID1="Cb8C401EFFc1b6fA" ID2="BB8Adaaf7Bf01DfB" />
    <CN ID1="FEae5648ECC0bf7d" ID2="7c8deBdbCd6D1FA1" />
    <CN ID1="fd6EeBB48cD832cB" ID2="80f3aCF0Dff3DAAF" />
    <CN ID1="7D4Cada4C4DD52E5" ID2="B75D8DfaBEe8742A" />
    <CN ID1="D4FC5DD8FeF5d5D1" ID2="8FdB58AE02A0C23f" />
    <CN ID1="2DCDBcde7eccC0ae" ID2="845af5C041AbAFf0" />
    <CN ID1="11ad710Da5551e1F" ID2="6Ae8A6Fa42AbAE3C" />
    <CN ID1="cF3f54c1d16bCB3a" ID2="A53BAbDA0AD1ABF8" />
    <CN ID1="cdF52EEBdd2bCFAd" ID2="cEDDF0761C5fCbEA" />
    <CN ID1="BbDC01bfd32B68a2" ID2="BB8Adaaf7Bf01DfB" />
    <CN ID1="165C8DDa0Af845b0" ID2="7c8deBdbCd6D1FA1" />
    <CN ID1="bEAE75275fFaef1c" ID2="a5E150AB38Fdc6F2" />
    <CN ID1="06ed6Ff5A27A8032" ID2="0dcFCBBA4bDEfCDC" />
    <CN ID1="5c800AFD0D3C5c1f" ID2="8FdB58AE02A0C23f" />
    <CN ID1="f26c6cD01C5Ef0bC" ID2="845af5C041AbAFf0" />
    <CN ID1="E1bBcfBAB40D55ae" ID2="6Ae8A6Fa42AbAE3C" />
    <CN ID1="BCa256267ae2080e" ID2="a2bf20432B7eEad8" />
    <CN ID1="eae03128E334Ebf0" ID2="BB8Adaaf7Bf01DfB" />
    <CN ID1="27cbcC4fdFe561F6" ID2="7c8deBdbCd6D1FA1" />
    <CN ID1="CCd7d4E7607F6408" ID2="ffB62B3B2feDB30E" />
    <CN ID1="AFA231Fa27241Edf" ID2="e4D5ebE5e7DeD5b5" />
    <CN ID1="2b8a26E5eFdFb055" ID2="2a8dD807AE351F4E" />
    <CN ID1="d5eb11b6B123bBB2" ID2="8FdB58AE02A0C23f" />
    <CN ID1="38E53BEf2B8b53c1" ID2="845af5C041AbAFf0" />
    <CN ID1="D52eb05bab2ae346" ID2="6Ae8A6Fa42AbAE3C" />
    <CN ID1="7D02CE7cc471bc08" ID2="eE5cb8c5A8Cf18a0" />
    <CN ID1="31Cf2fE50d07c54A" ID2="20cFACF1C4a17C7C" />
    <CN ID1="aDa63aAB1bdAf03A" ID2="BB8Adaaf7Bf01DfB" />
    <CN ID1="E7Ca4484ec8114BF" ID2="8FdB58AE02A0C23f" />
    <CN ID1="e3fA45F1ac6065af" ID2="845af5C041AbAFf0" />
    <CN ID1="60afBb8eDe10b236" ID2="6Ae8A6Fa42AbAE3C" />
    <CN ID1="badEDfE7F2b407FF" ID2="BB8Adaaf7Bf01DfB" />
    <CN ID1="3F76661cde8DAc6f" ID2="7c8deBdbCd6D1FA1" />
    <CN ID1="A5bec6D22CDbfE61" ID2="bF0dAaEcEAb3BA8d" />
    <CN ID1="eb75CCfAB8fCf5aB" ID2="44E36BC5bfdEC062" />
    <CN ID1="04d4B0D8067e20DA" ID2="eE033BF3a0DA7Cea" />
    <CN ID1="8bE84bFEeAEDDDFf" ID2="8FdB58AE02A0C23f" />
    <CN ID1="1aee400e3EAf23bE" ID2="845af5C041AbAFf0" />
    <CN ID1="2dAf308Fe20bbaFd" ID2="6Ae8A6Fa42AbAE3C" />
    <CN ID1="5B312A5EA2c4eabc" ID2="B1F1CfFCDAfA3A5D" />
    <CN ID1="88E2eE846FdaaAce" ID2="8bF583De2Eb04A6e" />
    <CN ID1="c602bEEE0DA6c1E8" ID2="8FdB58AE02A0C23f" />
    <CN ID1="DF82ffbEdAfc68Ad" ID2="845af5C041AbAFf0" />
    <CN ID1="81B5cEaEEac4db1f" ID2="6Ae8A6Fa42AbAE3C" />
    <CN ID1="B5A5A03ff60EdDEC" ID2="ae0DBC754cF3eB10" />
    <CN ID1="2Ca7cc2Cd3b3aFD1" ID2="BB8Adaaf7Bf01DfB" />
    <CN ID1="B116AFBecc8076f7" ID2="7c8deBdbCd6D1FA1" />
    <CN ID1="27b6672faf8e8b0C" ID2="BBACfaaaa4eCCfD3" />
    <CN ID1="B8ECfEA1Fe0beD3e" ID2="DcabD04D8B6bFdeb" />
    <CN ID1="E5f6c43BB28eF4Ce" ID2="BE1EA0C8E6fec1a1" />
    <CN ID1="F86f5fc17fAdCfe3" ID2="Dcd5ca040e05Ea2D" />
    <CN ID1="3f7827Bd1F3a0E5c" ID2="B32cF712Cab85874" />
    <CN ID1="eE705Ebfaa45dBde" ID2="8FdB58AE02A0C23f" />
    <CN ID1="Bcef2e8bA0BCeC78" ID2="845af5C041AbAFf0" />
    <CN ID1="2DfFf5Efd172cFaf" ID2="6Ae8A6Fa42AbAE3C" />
    <CN ID1="7E1b0B61da341Faf" ID2="a4Cae5cFC51febfb" />
    <CN ID1="6FD841Bf6Ac2FB01" ID2="8FdB58AE02A0C23f" />
    <CN ID1="05Da2b7fC7cB0Dba" ID2="845af5C041AbAFf0" />
    <CN ID1="b0D872DAdBdAeeb4" ID2="6Ae8A6Fa42AbAE3C" />
    <CN ID1="dBaeced8dF7ee734" ID2="c742c1e0C6bfbDdA" />
    <CN ID1="B0DeBFe86Bbf46fB" ID2="c0cDcCc36ecF814f" />
    <CN ID1="ca84A36Ea7DC8757" ID2="BB8Adaaf7Bf01DfB" />
    <CN ID1="06112bBb874BB655" ID2="7c8deBdbCd6D1FA1" />
    <CN ID1="fE5C468DFcc3f38e" ID2="dcB057FdcB0AFA3d" />
    <CN ID1="21A72Fd0130ba7Ff" ID2="BB8Adaaf7Bf01DfB" />
    <CN ID1="d364eBe2BDEE3312" ID2="7c8deBdbCd6D1FA1" />
    <CN ID1="AA57a0Ba28A3Ea12" ID2="6bd250b6dD2b66B2" />
    <CN ID1="0cAaf68Feefc6E54" ID2="dcfb66eC3EBDBbBE" />
    <CN ID1="1Df70eB1241a8faa" ID2="E6ebb5e725fcDfdD" />
    <CN ID1="1c5B8af4013f3a1F" ID2="8FdB58AE02A0C23f" />
    <CN ID1="46Bd4eBA8F2eCbbA" ID2="845af5C041AbAFf0" />
    <CN ID1="6F32DdB0dEA8Db61" ID2="6Ae8A6Fa42AbAE3C" />
    <CN ID1="1E4A8c20aA588d50" ID2="f13F84e70d8F3df0" />
    <CN ID1="aB2FF0d1Da8F8B7E" ID2="BB8Adaaf7Bf01DfB" />
    <CN ID1="CFDbC3B7dA7CbE4A" ID2="7c8deBdbCd6D1FA1" />
    <CN ID1="5DCdfE7fb68e2F8e" ID2="01e2de47EE0BBaCf" />
    <CN ID1="bA2d8ea5D1F7BA2c" ID2="16ab665A27cCaF22" />
  </Connections>
  <Notes>
    <Note ID="f7A62a58CcE1Fad6" X="483" Y="130" W="166" H="1001" Title="Values To Change" Text="This is the section that might need change from site to site as the structure names can be different. &#xD;&#xA;&#xD;&#xA;The struct processors use regex to read the correct structures so make sure this is correct." R="50" G="205" B="50" />
    <Note ID="b60EDDD120feCba6" X="867" Y="65" W="140" H="1214" Title="Warning! Do not change" Text="These nodes are used for the file names of the structures. And need to stay the same.&#xD;&#xA;&#xD;&#xA;This should not be changed. And if the structures are not working it is not because of these repeaters. More likely it is in the &quot;values to change column&quot;" R="255" G="69" B="0" />
  </Notes>
</MICE>