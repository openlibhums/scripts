<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                exclude-result-prefixes="xlink"
                version="1.0">

    <!-- Suppress the XML declaration -->
    <xsl:output method="html" indent="yes" omit-xml-declaration="yes"/>

    <!-- Match the abstract element and apply templates to all its children -->
    <xsl:template match="abstract">
        <xsl:apply-templates/>
    </xsl:template>

    <!-- Handle <p> -->
    <xsl:template match="p">
        <p><xsl:apply-templates/></p>
    </xsl:template>

    <!-- Handle <bold> -->
    <xsl:template match="bold">
        <strong><xsl:apply-templates/></strong>
    </xsl:template>

    <!-- Handle <italic> -->
    <xsl:template match="italic">
        <em><xsl:apply-templates/></em>
    </xsl:template>

    <!-- Handle <ext-link> with xlink:href -->
    <xsl:template match="ext-link">
        <a>
            <xsl:attribute name="href">
                <xsl:value-of select="@xlink:href"/>
            </xsl:attribute>
            <xsl:apply-templates/>
        </a>
    </xsl:template>

    <!-- Handle <xref> -->
    <xsl:template match="xref">
        <a href="#{@rid}">
            <xsl:apply-templates/>
        </a>
    </xsl:template>

    <!-- Handle <sub> -->
    <xsl:template match="sub">
        <sub><xsl:apply-templates/></sub>
    </xsl:template>

    <!-- Handle <sup> -->
    <xsl:template match="sup">
        <sup><xsl:apply-templates/></sup>
    </xsl:template>

    <!-- Handle <email> -->
    <xsl:template match="email">
        <a href="mailto:{.}">
            <xsl:apply-templates/>
        </a>
    </xsl:template>

    <!-- Default rule: copy the content -->
    <xsl:template match="*">
        <xsl:copy>
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>

    <!-- Handle text nodes -->
    <xsl:template match="text()">
        <xsl:value-of select="."/>
    </xsl:template>

</xsl:stylesheet>
