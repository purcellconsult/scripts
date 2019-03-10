########################################
# HTML tag generator script in python
# generates html tags from HTML element
# reference: https://www.w3schools.com/tags
#
# By Doug Purcell
# Website: http://www.purcellconsult.com
#
#
########################################

class html_generator:
    """ A simple class that generates html tags. """

    def generate_html_tag(self, input):

        tags = {

        'a': '<a href=""> </a>',
        'abbr': '<abbr> </abbr>',
        'acronym': '<acronym> </acronym>',
        'addr' : '<address> </address>',
        'app': '<applet> </applet>',
        'area': '<area> </area>',
        'article': '<article> </article>',
        'aside': '<aside> </aside>',
        'audio': '<audio> </audio>',
        'b': '<b> </b>',
        'base': '<base> </base>',
        'bdi': '<bdi> </bdi>',
        'bdo': '<bdo> </bdo>',
        'blockquote': '<blockquote> </blockquote>',
        'body': '<body> </body>',
        'br': '</br> ',
        'button': '<button> </button>',
        'canvas': '<canvas> </canvas>',
        'caption': '<caption> </caption>',
        'cite': '<cite> </cite>',
        'code': '<code> </code>',
        'col': '<col> </col>',
        'colgroup': '<colgroup> </colgroup>',
        'comment': '<!-- -->',
        'data': '<data> </data>',
        'datalist': '<datalist> </datalist>',
        'dd': '<dd> </dd>',
        'del': '<del> </del>',
        'details': '<details> </details>',
        'dfn': '<dfn> </dfn>',
        'dialog': '<dialog> </dialog>',
        'div': '<div> </div>',
        'dl': '<dl> </dl>',
        'dt': '<dt> </dt>',
        'em': '<em> </em>',
        'embed': '<embed> </embed>',
        'fieldset': '<fieldset> </fieldset>',
        'figcaption': '<figcaption> </figcaption>',
        'figure': '<figure> </figure>',
        'footer': '<footer> </footer>',
        'form': '<form> </form>',
        'h1': '<h1> </h1>',
        'h2': '<h2> </h2>',
        'h3': '<h3> </h3>',
        'h4': '<h4> </h4>',
        'h5': '<h5> </h5>',
        'h6': '<h6> </h6>',
        'head': '<head> </head>',
        'header': '<header> </header>',
        'hr': '<hr />',
        'html': '<html> </html>',
        'i': '<i> </i>',
        'iframe': '<iframe> </iframe>',
        'img': '<img> </img>',
        'input': '<input> </input>',
        'ins': '<ins> </ins>',
        'kbd': '<kbd> </kbd>',
        'label': '<label> </label>',
        'legend': '<legend> </legend>',
        'li': '<li> </li>',
        'link': '<link> </link>',
        'main': '<main> </main>',
        'map': '<map> </map>',
        'mark': '<mark> </mark>',
        'meta': '<meta> </meta>',
        'meter': '<meter> </meter>',
        'nav': '<nav> </nav>',
        'noscript': '<noscript> </noscript>',
        'object': '<object> </object>',
        'ol': '<ol> </ol>',
        'optgroup': '<optgroup> </optgroup>',
        'option': '<option> </option>',
        'output': '<output> </output>',
        'p': '<p> </p>',
        'param': '<param> </param>',
        'picture': '<picture> </picture>',
        'pre': '<pre> </pre>',
        'progress': '<progress> </progress>',
        'q': '<q> </q>',
        'rp': '<rp> </rp>',
        'rt': '<rt> </rt>',
        'ruby': '<ruby> </ruby>',
        's': '<s> </s>',
        'samp': '<samp> </samp>',
        'script': '<script> </script>',
        'section': '<section> </section>',
        'select': '<select> </select>',
        'small': '<small> </small>',
        'source': '<source> </source>',
        'span': '<span> </span>',
        'strong': '<strong> </strong>',
        'style': '<style> </style>',
        'sub': '<sub> </sub>',
        'summary': '<summary> </summary>',
        'sup': '<sup> </sup>',
        'svg': '<svg> </svg>',
        'table': '<table> </table>',
        'tbody': '<tbody> </tbody>',
        'td': '<td> </td>',
        'template': '<template> </template>',
        'textarea': '<textarea> </textarea>',
        'tfoot': '<tfoot> </tfoot>',
        'th': '<th> </th>',
        'thead': '<thead> </thead>',
        'time': '<time> </time>',
        'title': '<title> </title>',
        'tr': '<tr> </tr>',
        'track': '<track> </track>',
        'u': '<u> </u>',
        'ul': '<ul> </ul>',
        'var': '<var> </var>',
        'video': '<video> </video>',
        'wbr': '<wbr> </wbr>'

    }
        for x in tags.keys():
            if x == input:
                return tags[x]


if __name__ == '__main__':
    h = html_generator()
    html_tag = input("Enter html tag ")
    print(h.generate_html_tag(html_tag))
