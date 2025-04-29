<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" indent="yes" omit-xml-declaration="yes"/>

  <!-- Match article-title directly and apply templates to its children -->
  <xsl:template match="article-title">
    <xsl:apply-templates />
  </xsl:template>

  <!-- Valid inline JATS elements converted to HTML-style tags -->
  <xsl:template match="italic">
    <i><xsl:apply-templates /></i>
  </xsl:template>

  <xsl:template match="bold">
    <b><xsl:apply-templates /></b>
  </xsl:template>

  <xsl:template match="sup">
    <sup><xsl:apply-templates /></sup>
  </xsl:template>

  <xsl:template match="sub">
    <sub><xsl:apply-templates /></sub>
  </xsl:template>

  <xsl:template match="sc">
    <span style="font-variant: small-caps;"><xsl:apply-templates /></span>
  </xsl:template>

  <!-- Strip unhandled tags but preserve their content -->
  <xsl:template match="*">
    <xsl:apply-templates />
  </xsl:template>

</xsl:stylesheet>
