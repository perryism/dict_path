# Explore a json structure

<pre>
cat cloudtrail.json | python -m dictpath

{u'Records[]': [
   {
     u'Records[]/additionalEventData':
       {u'Records[]/additionalEventData/x-amz-id-2': <type 'unicode'>},
     u'Records[]/awsRegion': <type 'unicode'>,
     u'Records[]/eventID': <type 'unicode'>,
		 u'Records[]/eventName': <type 'unicode'>,
		 u'Records[]/eventSource': <type 'unicode'>,
		 u'Records[]/eventTime': <type 'unicode'>,
		 u'Records[]/eventType': <type 'unicode'>,
		 u'Records[]/eventVersion': <type 'unicode'>,
		 u'Records[]/readOnly': <type 'bool'>,
		 u'Records[]/recipientAccountId': <type 'unicode'>,
		 u'Records[]/requestID': <type 'unicode'>,
		 u'Records[]/requestParameters':
			 {u'Records[]/requestParameters/bucketName': <type 'unicode'>,
				u'Records[]/requestParameters/key': <type 'unicode'>,
				u'Records[]/requestParameters/partNumber': <type 'unicode'>,
				u'Records[]/requestParameters/uploadId': <type 'unicode'>},
		 u'Records[]/resources[]':
        [{u'Records[]/resources[]/ARN': <type 'unicode'>,
				  u'Records[]/resources[]/type': <type 'unicode'>}],
		 u'Records[]/responseElements': {u'Records[]/responseElements/x-amz-server-side-encryption': <type 'unicode'>},
		 u'Records[]/sourceIPAddress': <type 'unicode'>,
		 u'Records[]/userAgent': <type 'unicode'>,
		 u'Records[]/userIdentity':
        {u'Records[]/userIdentity/accessKeyId': <type 'unicode'>,
				 u'Records[]/userIdentity/accountId': <type 'unicode'>,
				 u'Records[]/userIdentity/arn': <type 'unicode'>,
				 u'Records[]/userIdentity/principalId': <type 'unicode'>,
				 u'Records[]/userIdentity/sessionContext':
            {u'Records[]/userIdentity/sessionContext/attributes':
              {u'Records[]/userIdentity/sessionContext/attributes/creationDate': <type 'unicode'>,
							  u'Records[]/userIdentity/sessionContext/attributes/mfaAuthenticated': <type 'unicode'>},
				     u'Records[]/userIdentity/sessionContext/sessionIssuer':
							 {u'Records[]/userIdentity/sessionContext/sessionIssuer/accountId': <type 'unicode'>,
								 u'Records[]/userIdentity/sessionContext/sessionIssuer/arn': <type 'unicode'>,
								 u'Records[]/userIdentity/sessionContext/sessionIssuer/principalId': <type 'unicode'>,
								 u'Records[]/userIdentity/sessionContext/sessionIssuer/type': <type 'unicode'>,
								 u'Records[]/userIdentity/sessionContext/sessionIssuer/userName': <type 'unicode'>},
						 u'Records[]/userIdentity/sessionContext/webIdFederationData':
               {u'Records[]/userIdentity/sessionContext/webIdFederationData/attributes':
                  {u'Records[]/userIdentity/sessionContext/webIdFederationData/attributes/cognito-identity.amazonaws.com:amr': <type 'unicode'>,
									 u'Records[]/userIdentity/sessionContext/webIdFederationData/attributes/cognito-identity.amazonaws.com:aud': <type 'unicode'>,
								   u'Records[]/userIdentity/sessionContext/webIdFederationData/attributes/cognito-identity.amazonaws.com:sub': <type 'unicode'>},
								   u'Records[]/userIdentity/sessionContext/webIdFederationData/federatedProvider': <type 'unicode'>}},
	 u'Records[]/userIdentity/type': <type 'unicode'>
  }
}]}
</pre>
